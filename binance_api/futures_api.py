'''
Endpoints are collected from the Futures Endpoint api section under the official binance api docs:
https://binance-docs.github.io/apidocs/spot/en/#futures
'''

# New Future Account Transfer:
class futures_transfer:
    params = {'R':['asset', 'amount', 'type']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/transfer'
    security_type = 'USER_DATA'


# Get Future Account Transaction History List :
class get_futures_transactions:
    params = {'R':['asset', 'startTime'],
            'O':['endTime', 'current', 'size']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/transfer'
    security_type = 'USER_DATA'


# Borrow For Cross-Collateral:
class borrow_crossCollat:
    params = {'R':['coin', 'amount', 'collateralCoin', 'collateralAmount']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/loan/borrow'
    security_type = 'TRADE'


# Cross-Collateral Borrow History:
class get_crossCollat_borrowHist:
    params = {'O':['coin', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/borrow/history'
    security_type = 'USER_DATA'


# Repay For Cross-Collateral:
class repay_crossCollat:
    params = {'R':['coin', 'collateralCoin', 'amount']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/loan/repay'
    security_type = 'USER_DATA'


# Cross-Collateral Repayment History:
class get_crossCollat_repayHist:
    params = {'R':['coin', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/repay/history'
    security_type = 'USER_DATA'


# Cross-Collateral Wallet:
class get_crossCollat_wallet:
    params = None
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/wallet'
    security_type = 'USER_DATA'


# Cross-Collateral Wallet V2:
class get_crossCollat_wallet_v2:
    params = None
    method = 'GET'
    endpoint = '/sapi/v2/futures/loan/wallet'
    security_type = 'USER_DATA'


# Cross-Collateral Information:
class get_crossCollat_info:
    params = {'O':['collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/configs'
    security_type = 'USER_DATA'


# Cross-Collateral Information V2:
class get_crossCollat_info_v2:
    params = {'O':['loanCoin', 'collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v2/futures/loan/configs'
    security_type = 'USER_DATA'


# Calculate Rate After Adjust Cross-Collateral LTV:
class get_crossCollat_rate_LTV:
    params = {'R':['collateralCoin', 'amount', 'direction']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/calcAdjustLevel'
    security_type = 'USER_DATA'


# Calculate Rate After Adjust Cross-Collateral LTV V2:
class get_crossCollat_rate_LTV_v2:
    params = {'R':['loanCoin', 'collateralCoin', 'amount', 'direction']}
    method = 'GET'
    endpoint = '/sapi/v2/futures/loan/calcAdjustLevel'
    security_type = 'USER_DATA'


# Get Max Amount for Adjust Cross-Collateral LTV:
class get_crossCollat_max_LTV:
    params = {'R':['collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/calcMaxAdjustAmount'
    security_type = 'USER_DATA'


# Get Max Amount for Adjust Cross-Collateral LTV V2:
class get_crossCollat_max_LTV_v2:
    params = {'R':['loanCoin', 'collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v2/futures/loan/calcMaxAdjustAmount'
    security_type = 'USER_DATA'


# Adjust Cross-Collateral LTV:
class adjust_crossCollat_LTV:
    params = {'R':['collateralCoin', 'amount', 'direction']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/loan/adjustCollateral'
    security_type = 'TRADE'


# Adjust Cross-Collateral LTV V2:
class adjust_crossCollat_LTV_v2:
    params = {'R':['loanCoin', 'collateralCoin', 'amount', 'direction']}
    method = 'POST'
    endpoint = '/sapi/v2/futures/loan/adjustCollateral'
    security_type = 'TRADE'


# Adjust Cross-Collateral LTV History:
class adjust_crossCollat_LTV_history:
    params = {'O':['loanCoin', 'collateralCoin', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/adjustCollateral/history'
    security_type = 'USER_DATA'


# Cross-Collateral Liquidation History:
class adjust_crossCollat_liquidation_history:
    params = {'O':['loanCoin', 'collateralCoin', 'startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/liquidationHistory'
    security_type = 'USER_DATA'


# Check Collateral Repay Limit:
class get_collatRepay_limit:
    params = {'R':['coin', 'collateralCoin']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/collateralRepayLimit'
    security_type = 'USER_DATA'


# Get Collateral Repay Quote:
class get_collatRepay_quote:
    params = {'R':['coin', 'collateralCoin', 'amount']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/collateralRepay'
    security_type = 'USER_DATA'


# Repay with Collateral:
class collateral_repay:
    params = {'R':['quoteId']}
    method = 'POST'
    endpoint = '/sapi/v1/futures/loan/collateralRepay'
    security_type = 'USER_DATA'


# Collateral Repayment Result:
class get_collatRepay_result:
    params = {'R':['quoteId']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/collateralRepayResult'
    security_type = 'USER_DATA'


# Cross-Collateral Interest History:
class get_crossCollat_interestHist:
    params = {'O':['collateralCoin', 'startTime', 'endTime', 'current', 'limit']}
    method = 'GET'
    endpoint = '/sapi/v1/futures/loan/interestHistory'
    security_type = 'USER_DATA'

#Leverage information of symbols
class get_leverage_brackets:
    params = {'R':['timestamp'],
              'O':['symbol', 'recvWindow']}
    method = 'GET'
    endpoint= '/fapi/v1/leverageBracket'
    security_type = 'USER_DATA'
    base = 'https://fapi.binance.com'

#Info on futures candle
class get_future_candles:
    params = {'R':['symbol', 'interval'],
            'O':['startTime', 'endTime', 'limit']}
    method = 'GET'
    endpoint = '/fapi/v1/klines'
    security_type = 'None'
    base = 'https://fapi.binance.com'

class post_multiple_orders:
    params = {'R':['batchOrders', 'timestamp'],
            'O':['recvWindow']}
    method = 'POST'
    endpoint = '/fapi/v1/batchOrders'
    security_type = 'TRADE' 
    base = 'https://fapi.binance.com'

class get_future_24h_ticker:
    params = {'O': ['symbol']}
    method = 'GET'
    endpoint = '/fapi/v1/ticker/24hr'
    base = 'https://fapi.binance.com'
    security_type = 'None'

class get_future_depth:
    params = {'R':['symbol'],
            'O':['limit']}
    method = 'GET'
    endpoint = '/fapi/v1/depth'
    security_type = 'None'
    base = 'https://fapi.binance.com'

class get_mark_price:
    params = {'O': ['symbol']}
    method = 'GET'
    endpoint = '/fapi/v1/premiumIndex'
    base = 'https://fapi.binance.com'
    security_type = 'None'
class change_initial_lev :
    params = {'R': ['symbol', 'leverage', 'timestamp']}
    method = 'POST'
    endpoint = '/fapi/v1/leverage'
    base = 'https://fapi.binance.com'
    security_type = 'TRADE'
class cancel_all_order:
    params = {'R': ['symbol', 'timestamp']}
    method = 'DELETE'
    endpoint = '/fapi/v1/allOpenOrders'
    base = 'https://fapi.binance.com'
    security_type = 'TRADE'
