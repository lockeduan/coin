"""
:short_ratio: each time short ratio
:long_total_ratio:: percent of money that every time long
:long_price_down_ratio:: price down ratio since last dead cross of EMA, only when reach this ratio then long
"""
url_cn = "www.okcoin.cn"
url_com = "www.okcoin.com"
log_path = "c:\logs"
signal_test_log_path = "c:\logs\stlogs"

LONG_PRICE_DOWN_RATIO = 'long_price_down_ratio'

config_1min = {
    "stop_profit_ratio": 0.025,
    "stop_loss_ratio": 0.045,
    "short_ratio": [0.2, 0.3, 0.5],
    "coin_most_hold_ratio": 0.35,
    "long_total_ratio": 0.3,
    "long_price_down_ratio": 0.025,
    "lock_profit_ratio": 0.02,
    "stop_loss_count_down": 1,
    "give_up_long_count_down": 2
}

config_3min = {
    "stop_profit_ratio": 0.025,
    "stop_loss_ratio": 0.045,
    "short_ratio": [0.2, 0.3, 0.5],
    "coin_most_hold_ratio": 0.35,
    "long_total_ratio": 0.3,
    "long_price_down_ratio": 0.025,
    "lock_profit_ratio": 0.02,
    "stop_loss_count_down": 1,
    "give_up_long_count_down": 2
}

config_5min = {
    "stop_profit_ratio": 0.04,
    "stop_loss_ratio": 0.045,
    "short_ratio": [0.2, 0.3, 0.5],
    "coin_most_hold_ratio": 0.3,
    "long_total_ratio": 0.3,
    "long_price_down_ratio": 0.03,
    "lock_profit_ratio": 0.02,
    "stop_loss_count_down": 1,
    "give_up_long_count_down": 2
}

eamcrosswithmacd_config_1min = {
    "assistant_type": "3min",
    "stop_loss_ratio": 0.1,
    "stop_profit_btc": 0.01,
    "stop_profit_eth": 0.01,
    "stop_profit_ltc": 0.01,
    "lock_profit_btc": 0.02,
    "lock_profit_eth": 0.02,
    "lock_profit_ltc": 0.02,
    "short_ratio": [0.6, 1],
    "coin_most_hold_ratio": 0.33,
    "long_total_ratio": 0.1,
    "long_price_down_ratio": 0.01,
    "advance_long_down_ratio": 0.02,
    "stop_loss_count_down": 3,
    "on_ranging": 0.0013,
    "macd_long_price_threshold": 0.01,
    "four_green_price_threshold": 0.008,#four green bar price rised should not excees this
    "four_green_price_single_threshold": 0.005, #each of four green bar price should not excess this
    "ema_quick_periods": 9,
    "ema_slow_periods": 21
}

eamcrosswithmacd_config_3min = {
    "assistant_type": "15min",
    "stop_loss_ratio": 0.1,
    "stop_profit_btc": 0.02,
    "stop_profit_eth": 0.02,
    "stop_profit_ltc": 0.02,
    "lock_profit_btc": 0.05,
    "lock_profit_eth": 0.05,
    "lock_profit_ltc": 0.05,
    "short_ratio": [0.6, 1],
    "coin_most_hold_ratio": 0.33,
    "long_total_ratio": 0.1,
    "long_price_down_ratio": 0.025,
    "advance_long_down_ratio": 0.03,
    "stop_loss_count_down": 2,
    "on_ranging": 0.0013,
    "macd_long_price_threshold": 0.01,
    "four_green_price_threshold": 0.01,
    "four_green_price_single_threshold": 0.005,
    "ema_quick_periods": 9,
    "ema_slow_periods": 21
}

eamcrosswithmacd_config_5min = {
    "assistant_type": "15min",
    "stop_loss_ratio": 0.1,
    "stop_profit_btc": 0.01,
    "stop_profit_eth": 0.01,
    "stop_profit_ltc": 0.01,
    "lock_profit_btc": 0.035,
    "lock_profit_eth": 0.035,
    "lock_profit_ltc": 0.035,
    "short_ratio": [0.6, 1],
    "coin_most_hold_ratio": 0.33,
    "long_total_ratio": 0.1,
    "long_price_down_ratio": 0.025,
    "advance_long_down_ratio": 0.03,
    "stop_loss_count_down": 2,
    "on_ranging": 0.0013,
    "macd_long_price_threshold": 0.01,
    "four_green_price_threshold": 0.01,
    "four_green_price_single_threshold": 0.005,
    "ema_quick_periods": 9,
    "ema_slow_periods": 21
}