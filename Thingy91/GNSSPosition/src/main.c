/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
 */

#include <stdio.h>
#include <zephyr/kernel.h>

#include <zephyr/logging/log.h>
#include <modem/lte_lc.h>
#include <dk_buttons_and_leds.h>

/* STEP 4 - Include the header file for the GNSS interface */
#include <nrf_modem_gnss.h>

/* STEP 5 - Define the PVT data frame variable */
static struct nrf_modem_gnss_pvt_data_frame pvt_data;

/* STEP 12.1 - Declare helper variables to find the TTFF */
static int64_t gnss_start_time;
static bool first_fix = false;

static K_SEM_DEFINE(lte_connected, 0, 1);

LOG_MODULE_REGISTER(Lesson6_Exercise1, LOG_LEVEL_INF);

static void lte_handler(const struct lte_lc_evt *const evt)
{
	switch (evt->type) {
	case LTE_LC_EVT_NW_REG_STATUS:
		if ((evt->nw_reg_status != LTE_LC_NW_REG_REGISTERED_HOME) &&
			(evt->nw_reg_status != LTE_LC_NW_REG_REGISTERED_ROAMING)) {
			break;
		}
		LOG_INF("Network registration status: %s",
				evt->nw_reg_status == LTE_LC_NW_REG_REGISTERED_HOME ?
				"Connected - home network" : "Connected - roaming");
		k_sem_give(&lte_connected);
		break;
	case LTE_LC_EVT_RRC_UPDATE:
		LOG_INF("RRC mode: %s", evt->rrc_mode == LTE_LC_RRC_MODE_CONNECTED ? 
				"Connected" : "Idle");
		break;	
	default:
		break;
	}
}

static void modem_configure(void)
{
	LOG_INF("Connecting to LTE network");

	int err = lte_lc_init_and_connect_async(lte_handler);
	if (err) {
		LOG_ERR("Modem could not be configured, error: %d", err);
		return;
	}
	k_sem_take(&lte_connected, K_FOREVER);
	LOG_INF("Connected to LTE network");
	dk_set_led_on(DK_LED2);
}

/* STEP 6 - Define a function to log fix data in a readable format */
static void print_fix_data(struct nrf_modem_gnss_pvt_data_frame *pvt_data)
{
	// LOG_INF("Latitude:       %.06f", pvt_data->latitude);
	// LOG_INF("Longitude:      %.06f", pvt_data->longitude);
	// LOG_INF("Altitude:       %.01f m", pvt_data->altitude);
	// LOG_INF("Time (UTC):     %02u:%02u:%02u.%03u",
	//        pvt_data->datetime.hour,
	//        pvt_data->datetime.minute,
	//        pvt_data->datetime.seconds,
	//        pvt_data->datetime.ms);
	printk("\n%02u:%02u:%02u.%03u,%.06f,%.06f,%.01f", 
		pvt_data->datetime.hour,
		pvt_data->datetime.minute,
		pvt_data->datetime.seconds,
		pvt_data->datetime.ms,
		pvt_data->latitude, 
		pvt_data->longitude, 
		pvt_data->altitude);
}


static void gnss_event_handler(int event)
{
	int err;

	switch (event) {
	/* STEP 7 - On a PVT event, confirm if PVT data is a valid fix */
	case NRF_MODEM_GNSS_EVT_PVT:
		if(!first_fix) {
			LOG_INF("Searching...");
		}
		/* STEP 15 - Print satellite information */
		int num_satellites = 0;
		for (int i = 0; i < 12 ; i++) {
			if (pvt_data.sv[i].signal != 0) {
				if(!first_fix) {
					LOG_INF("sv: %d, cn0: %d", pvt_data.sv[i].sv, pvt_data.sv[i].cn0);
				}
				num_satellites++;
			}	
		} 
		if(!first_fix) {
			LOG_INF("Number of current satellites: %d", num_satellites);
		}
		err = nrf_modem_gnss_read(&pvt_data, sizeof(pvt_data), NRF_MODEM_GNSS_DATA_PVT);
		if (err) {
			LOG_ERR("nrf_modem_gnss_read failed, err %d", err);
			return;
		}
		// if (pvt_data.flags & NRF_MODEM_GNSS_PVT_FLAG_DEADLINE_MISSED) {
		// 	LOG_INF("GNSS blocked by LTE activity");
		// } if (pvt_data.flags & NRF_MODEM_GNSS_PVT_FLAG_NOT_ENOUGH_WINDOW_TIME) {
		// 	LOG_INF("Insufficient GNSS time windows");
		// }
		if (pvt_data.flags & NRF_MODEM_GNSS_PVT_FLAG_FIX_VALID) {
			dk_set_led_on(DK_LED1);
			print_fix_data(&pvt_data);
			/* STEP 12.3 - Print the time to first fix */
			if (!first_fix) {
				LOG_INF("Time to first fix: %2.1lld s", (k_uptime_get() - gnss_start_time)/1000);
				first_fix = true;
				LOG_INF("\nTime,Latitude,Longitude,Altitude");
			}
			return;
		}
		break;
	/* STEP 7.2 - Log when the GNSS sleeps and wakes up */
	case NRF_MODEM_GNSS_EVT_PERIODIC_WAKEUP:
		//LOG_INF("GNSS has woken up");
		break;
	case NRF_MODEM_GNSS_EVT_SLEEP_AFTER_FIX:
		//LOG_INF("GNSS enter sleep after fix");
		break;
	default:
		break;
	}
}

void main(void)
{

	if (dk_leds_init() != 0) {
		//LOG_ERR("Failed to initialize the LEDs Library");
	}

	modem_configure();
	
	/* STEP 8 - Activate modem and deactivate LTE */
	if (lte_lc_func_mode_set(LTE_LC_FUNC_MODE_NORMAL) != 0) {
		//LOG_ERR("Failed to activate GNSS functional mode");
		return;
	}	
	
	LOG_INF("Deactivating LTE");
	if (lte_lc_func_mode_set(LTE_LC_FUNC_MODE_DEACTIVATE_LTE) != 0) {
		//LOG_ERR("Failed to activate GNSS functional mode");
		return;
	}

	/* STEP 9 - Register the GNSS event handler */
	if (nrf_modem_gnss_event_handler_set(gnss_event_handler) != 0) {
		//LOG_ERR("Failed to set GNSS event handler");
		return;
	}

	/* STEP 10 - Set the GNSS fix interval and GNSS fix retry period */
	if (nrf_modem_gnss_fix_interval_set(CONFIG_GNSS_PERIODIC_INTERVAL) != 0) {
		//LOG_ERR("Failed to set GNSS fix interval");
		return;
	}

	if (nrf_modem_gnss_fix_retry_set(CONFIG_GNSS_PERIODIC_TIMEOUT) != 0) {
		//LOG_ERR("Failed to set GNSS fix retry");
		return;
	}

	/* STEP 11 - Start the GNSS receiver*/
	//LOG_INF("Starting GNSS");
	if (nrf_modem_gnss_start() != 0) {
		//LOG_ERR("Failed to start GNSS");
		return;
	}	

	/* STEP 12.2 - Log the current system uptime */
	gnss_start_time = k_uptime_get();
}