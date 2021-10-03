# 추가할 것들....   1. 지갑이 여러개 닫혔을 경우 어느것을 매수할 것인지?   2. 타거래소 지갑감지 시스템
import pandas as pd
import time
import datetime
import telegram
import pyupbit   # upbit API
import ccxt      # binance API
import pybithumb # bithumb API
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import math
import tweepy

# 텔레그램 binanaceBot Api
TG_token = 
token = TG_token
id = 
bot = telegram.Bot(token)

# 텔레그램 binanceBuyBot Api
TG_token2 =
token2 = TG_token2
id2 =
buy_bot = telegram.Bot(token2)

# upbit Api
access_key =
secret_key = 
server_url = 'https://api.upbit.com'

upbit = pyupbit.Upbit(access_key, secret_key)

# bithumb Api
bithumb_connect_key = 
bithumb_secret_key =

# 빗썸 aws용 api


bithumb = pybithumb.Bithumb(bithumb_connect_key, bithumb_secret_key)

# binance (현물) Api
binance = 
# binance (현물) Api

# huobi Api
huobi = ccxt.huobipro()


# coin List #

# upbit coinList (BTC/KRW)
upbit_coinList = ["LTC","BCHA","ELF","GLM","BTT","ETC","ADA","DOGE","BTG","BSV","MTL","SRM","AXS","IOTA","SAND","STX","JST","FCT2","WAXP","KAVA","HIVE","FLOW","TRX","VET","EOS","DAWN","BCH","POWR","AQT","PLA","WAVES","QTUM","HBAR","CBK","OMG","TON","BORA","IOST","MLK","GAS","TRUEL","RFR","HUNT","ATOM","SNT","MED","NEO","UPP","MOC","PUNDIX","ONG","IQ","HUM","AHT","ORBS","SSX","STRAX","MANA","XEM","XTZ","STRK","REP","CVC","ICX","META","SXP","TT","LOOM","THETA","STEEM","ENJ","CHZ","ZIL","MVL","AERGO","SC","MBL","LSK","ARDR","CRE","STMX","SBD","ANKR","STORJ","DKA","LNC","ONT","POLY","QKC","GRS","MFT","ARK","STPT","BAT","ZRX","KNC","LINK"]
upbit_BTC_coinList = ["CELO","LRC","ONIT","FOR","RVN","FIL","DAD","BNT","SNX","LUNA","PSG","NKN","RLC","CRV","HBD","DGB","PROM","LINA","RSR","NMR","ALGO","DNT","INJ","CTSI","SUN","CHR","AUCTION","GO","GXC","UNI","NEAR","BASIC","JUV","GRT","OXT","OGN","COMP","DENT","MKR","SOLVE"]
upbit_BTC_wallet_coinList = ["MKR","COMP","NMR","JUV","PSG","AUCTION","UNI","PROM","INJ","SNX","NEAR","VAL","ALGO","CELO","BNT","RLC","CRV","PAX","DAI","HBD","OGN","GRT","FX","GXC","CTSI","LRC","NKN","OXT","CHR","BFC","DAD","DNT","ONIT","IOTX","FOR","DGB","LINA","RSR","SUN","GO","SOLVE"]

# bithumb  wallet_coinList
bithumb_wallet_coinList = ["LOOM","LF","BIOT","WEMIX","MSB","NU","UMA","ANV","VELO","ASM","ALICE","TEMCO","MM","VRA","MVC","WTC","DVI","SUN","SOC","REN","XNO","CELR","XPR","COS","YFI","BTG","HIVE","ELF","AWO","RLC","MANA","KNC","MLK","ORC","ADP","EL","ORBS","CAKE","LPT","FX","PUNDIX","BURGER","ZRX","MATIC","HDAC","GOM2","RSR","BORA","BFC","WAXP","PCI","KSM","QTCON","BOA","OXT","REP","FCT","QKC","CKB","BAL","GRT","TRV","BCD","CYCLUB","LRC","RINGX","UOS","MIR","CTXC","GHX","CENNZ","AAVE","NMR","MAP","XYM","OCEAN","RAI","AION","WOM","GXC","EVZ","HIBS","EM","MXC","DAD","VALOR","ARPA","FLETA","BNT","LINA","CHR","TRUE","APIX","COMP","CTSI","BEL","WIKEN","MKR","XVS","WOZX","DAI","BAKE","BLY","WICC","CTK","BAT"]
bithumb_coinList = bithumb.get_tickers() # 빗썸 전체 코인 가져옴
# binance future coinList
binance_future_coinList = ["1INCH/USDT","AAVE/USDT","ADA/USDT","AKRO/USDT","ALGO/USDT","ALICE/USDT","ALPHA/USDT","ANKR/USDT","ATOM/USDT","AVAX/USDT","AXS/USDT","BAKE/USDT","BAL/USDT","BAND/USDT","BAT/USDT","BCH/USDT","BEL/USDT","BLZ/USDT","BNB/USDT","BTS/USDT","BZRX/USDT","BTT/USDT","CELR/USDT","CHR/USDT","CHZ/USDT","COMP/USDT","COTI/USDT","CRV/USDT","CTK/USDT","CVC/USDT","DASH/USDT","DENT/USDT","DGB/USDT","DODO/USDT","DOGE/USDT","DOT/USDT","EGLD/USDT","ENJ/USDT","EOS/USDT","ETC/USDT","FIL/USDT","FLM/USDT","FTM/USDT","GRT/USDT","GTC/USDT","HBAR/USDT","HNT/USDT","HOT/USDT","ICP/USDT","ICX/USDT","IOST/USDT","IOTA/USDT","KAVA/USDT","KEEP/USDT","KNC/USDT","KSM/USDT","LINA/USDT","LINK/USDT","LIT/USDT","LRC/USDT","LTC/USDT","LUNA/USDT","MANA/USDT","MATIC/USDT","MKR/USDT","MTL/USDT","NEAR/USDT","NEO/USDT","NKN/USDT","OCEAN/USDT","OGN/USDT","OMG/USDT","ONE/USDT","ONT/USDT","QTUM/USDT","REEF/USDT","REN/USDT","RLC/USDT","RSR/USDT","RUNE/USDT","RVN/USDT","SAND/USDT","SFP/USDT","SKL/USDT","SNX/USDT","SOL/USDT","SRM/USDT","STMX/USDT","STORJ/USDT","SUSHI/USDT","SXP/USDT","THETA/USDT","TLM/USDT","TOMO/USDT","TRB/USDT","TRX/USDT","UNFI/USDT","UNI/USDT","VET/USDT","WAVES/USDT","XEM/USDT","XLM/USDT","XMR/USDT","XRP/USDT","XTZ/USDT","ZEC/USDT","ZEN/USDT","ZIL/USDT","ZRX/USDT"]

# huobi coinList
huobi_coinList = huobi.fetch_tickers()


# user agent
headers = {}

# 바이낸스 현물 코인 가격의 변화를 확인하는 메소드
#def binance_Coin_price_change(binance_coin):



# 바이낸스 선물 코인 가격의 변화를 확인하는 메소드
#def binance_future_Coin_price_change(binance_future_coin):

current_notice = None  # 최근 공지

notice = None


# 프로그램 첫 실행시 가장 최근의 공지를 저장함


options = webdriver.ChromeOptions()                    # 크롬옵션 설정
options.headless = True                                # headless로 설정
options.add_argument("window-size=1920x1080")          # (" ")안에 자기가 쓰는 모니터의 화면크기 입력
# Headless로 인한 사이트 접근이 막히는걸 방지하기 위해서 add_argument로 user_agent를 적용해주어야 할 수 있다.
options.add_argument()

browser = webdriver.Chrome('여기는 크롬드라이버잇는 ', options=options)

browser.get("https://t.me/s/shrimp_notice")
notices = browser.find_elements_by_tag_name("div")

for i in range(1,30):
    if("업비트" in notices[-i].text or "바이낸스" in notices[-i].text or "빗썸" in notices[-i].text or "코인베이스" in notices[-i].text or "코인원" in notices[-i].text or "후오비" in notices[-i].text or "고팍스" in notices[-i].text):
            current_notice = notices[-i].text
            break

print(current_notice)

bot.sendMessage(chat_id=id,text=str(datetime.datetime.now())+"\n"+"\n"+current_notice)

time.sleep(1)

while(1):

    try:
        # 공지사항

        time.sleep(0.3)

        browser.get("https://t.me/s/shrimp_notice")
        notices = browser.find_elements_by_tag_name("div")

        # 가장 최근 공지을 스크래핑
        for i in range(1,30):
            if("업비트" in notices[-i].text or "바이낸스" in notices[-i].text or "빗썸" in notices[-i].text or "코인베이스" in notices[-i].text or "코인원" in notices[-i].text or "후오비" in notices[-i].text or "고팍스" in notices[-i].text):
                notice = notices[-i].text
                break
        
        if(notice!=current_notice): # 최근 공지가 새로운 공지일 경우
            print("    ")
            print("     <<<<< New notice >>>>>     ")
            print(notice)

            # case 1) 업비트 입출금 공지사항
            if("업비트" in notice and ("입출금" in notice or "입금" in notice)):
                if("(완료)" in notice or "재개합니다"in notice):
                    for coin in upbit_BTC_wallet_coinList:   # 지갑 닫히면 쏘는 코인들을 선정하여서 넣어둔 walletcoinlist
                        if(str(coin) in notice): 
                            wallet_coin = upbit.get_balance("BTC-"+str(coin))
                            if(wallet_coin>0): # 지갑닫혀서 매수했던 코인을 아직 홀딩하고있을 경우 시장가로 던짐
                                upbit.sell_market_order("BTC-"+str(coin),wallet_coin)
                                while(1):
                                    try:
                                        buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"입출금 완료 공지므로 매도하였습니다.")
                                        break
                                    except:
                                        print("re-message")
                                        continue

                            else: # 매수하지 않았다면 그냥 지갑완료 공지라고 메세지를 보냄
                                while(1):
                                    try:
                                        buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"입출금 완료 공지므로 매수하지 않았습니다.")
                                        break
                                    except:
                                        print("re-message")
                                        continue                                


                else: # 지갑이 닫힌 거라면
                    for coin in upbit_BTC_wallet_coinList:   # 지갑 닫히면 쏘는 코인들을 선정하여서 넣어둔 walletcoinlist
                        if(str(coin) in notice):
                            KRW_seed = upbit.get_balance("KRW")
                            upbit.buy_market_order("KRW-BTC",KRW_seed*0.995)
                            time.sleep(0.2)
                            BTC_seed = upbit.get_balance("KRW-BTC")
                            upbit.buy_market_order("BTC-"+str(coin),BTC_seed*0.994)
                            time.sleep(0.3)
                            
                            while(1): # 매수하였으므로 telegram으로 메세지
                                try:
                                    buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+str(coin)+" 입출금이 닫혔으므로 매수하였습니다.")
                                    break
                                except:
                                    print("re-message")
                                    continue
                            

            # case 2) 빗썸 입출금 공지사항
            elif("빗썸" in notice and (("입출금" in notice) or ("입금" in notice))):
                if("재개)" in notice or "재개합니다" in notice or "투자유의" in notice or "거래지원종료" in notice): # 입출금 중지가 아닌 알림
                    while(1):
                        try:
                            buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"입출금이 닫힌 공지가 아니므로 매수하지 않았습니다.")
                            break
                        except:
                            print("re-message")
                            continue

                else: # 지갑이 닫힌 거라면         * bitthumb의 경우 최소거래수량이 정해져 있어 아래와같이 코드를 실행
                    for coin in bithumb_wallet_coinList:
                        
                        buy_count = 0

                        if(str(coin) in notice): 
                            while(buy_count<3): # 총 3번 나누어 매수

                                buy_count+=1 

                                KRW_seed = bithumb.get_balance("BTC")[2] # 가지고있는 원화량

                                orderbook = pybithumb.get_orderbook(str(coin)) # 오더북
                                sell_price = orderbook['asks'][0]['price'] # 시장가 조회
                                unit = KRW_seed/float(sell_price)*0.70 # 살수 있는 물량

                                if(sell_price<100): # 코인가격이 100원 미만일 경우       100
                                    unit = int(unit/100)*100
                                    bithumb.buy_market_order(str(coin),unit)
                      
                                
                                elif(sell_price<1000): # 코인가격이 1000원 미만일 경우    10
                                    unit = int(unit/10)*10
                                    bithumb.buy_market_order(str(coin),unit)
                                    
                                elif(sell_price<10000): # 코인가격이 10000원 미만일 경우   1
                                    unit = int(unit)
                                    bithumb.buy_market_order(str(coin),unit)
                                    
                                elif(sell_price<100000): # 코인가격이 100000원 미만일 경우  0.1
                                    round_unit = round(unit,1) # 1까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.1)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        

                                elif(sell_price<1000000): # 코인가격이 1000000원 미만일 경우 0.01
                                    round_unit = round(unit,2) # 2까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.01)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        
                                elif(sell_price<10000000): # 코인가격이 10000000.....   0.001
                                    round_unit = round(unit,3) # 3까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.001)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        
                                else: # 코인가격이 10000000.....   0.0001
                                    round_unit = round(unit,4) # 4까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.0001)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                            
                            while(1): # buyboy ->
                                try:
                                    buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+str(coin)+" 입출금이 중지되었으므로 매수하였습니다.")
                                    break
                                except:
                                    print("re-message")
                                    continue
                            

            # 바이낸스 상장 공시                      (Ex) Binance will list .... crypto    ---> BUY )      
            elif("바이낸스" in notice):
                if("List" in notice and (("Delist" in notice)==False)):
                    # huobi_Coin
                    for coin in huobi_coinList:
                        if("/USDT" in coin):
                            coin_symbol = coin[:-5] # USDT를 빼기 심볼 자체만
                            
                            if(coin_symbol in notice):
                                seed = huobi.fetch_balance()["USDT"]["free"]

                                df = huobi.fetch_ohlcv(coin_symbol+str("/USDT"),"1m")
                                coin_current_price = df[-1][4] # 현재가
                                huobi.create_market_buy_order(coin_symbol+"/USDT",seed/coin_current_price*0.95)

                                while(1):
                                    try:
                                        buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"(Huobi) "+str(coin)+" 바이낸스 상장 -> 매수하였습니다.")
                                        break
                                    except:
                                        print("re-message")
                                        continue
                                    
                    # upbit_Coin 
                    for coin in upbit_coinList: # 공지에 언급된 upbit코인이 있는지 확인
                        if(str(coin) in notice): # 공지에 코인이 언급되있을 경우 바로 매수
                            KRW_seed = upbit.get_balance("KRW")
                            upbit.buy_market_order("KRW-"+str(coin),KRW_seed*0.995)
                            while(1):
                                try:
                                    buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"(Upbit) "+str(coin)+" 바이낸스 상장 -> 매수하였습니다.")
                                    break
                                except:
                                    print("re-message")
                                    continue
                        
                
                    # upbit_Coin BTC
                    for coin in upbit_BTC_coinList: # 공지에 언급된 upbit코인이 있는지 확인
                        if(str(coin) in notice): # 공지에 코인이 언급되있을 경우
                            KRW_seed = upbit.get_balance("KRW")
                            upbit.buy_market_order("KRW-BTC",KRW_seed*0.995)
                            time.sleep(0.2)
                            BTC_seed = upbit.get_balance("KRW-BTC")
                            upbit.buy_market_order("BTC-"+str(coin),BTC_seed*0.994)
                            while(1):
                                try:
                                    buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"(Upbit) "+str(coin)+" 바이낸스 상장 -> 매수하였습니다.")
                                    break
                                except:
                                    print("re-message")
                                    continue


                    # bithumb_Coin
                    for coin in bithumb_coinList:
                        if(str(coin) in notice):
                           
                            buy_count = 0

                            while(buy_count<3): # 총 3번 나누어 매수

                                buy_count+=1 

                                KRW_seed = bithumb.get_balance("BTC")[2] # 가지고있는 원화량

                                orderbook = pybithumb.get_orderbook(str(coin)) # 오더북
                                sell_price = orderbook['asks'][0]['price'] # 시장가 조회
                                unit = KRW_seed/float(sell_price)*0.70 # 살수 있는 물량

                                if(sell_price<100): # 코인가격이 100원 미만일 경우       100
                                    unit = int(unit/100)*100
                                    bithumb.buy_market_order(str(coin),unit)
                        
                                
                                elif(sell_price<1000): # 코인가격이 1000원 미만일 경우    10
                                    unit = int(unit/10)*10
                                    bithumb.buy_market_order(str(coin),unit)
                                    
                                elif(sell_price<10000): # 코인가격이 10000원 미만일 경우   1
                                    unit = int(unit)
                                    bithumb.buy_market_order(str(coin),unit)
                                    
                                elif(sell_price<100000): # 코인가격이 100000원 미만일 경우  0.1
                                    round_unit = round(unit,1) # 1까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.1)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        

                                elif(sell_price<1000000): # 코인가격이 1000000원 미만일 경우 0.01
                                    round_unit = round(unit,2) # 2까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.01)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        
                                elif(sell_price<10000000): # 코인가격이 10000000.....   0.001
                                    round_unit = round(unit,3) # 3까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.001)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        
                                else: # 코인가격이 10000000.....   0.0001
                                    round_unit = round(unit,4) # 4까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.0001)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                            while(1):
                                try:
                                    buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"(Bithumb) "+str(coin)+" 바이낸스 상장 -> 매수하였습니다.")
                                    break
                                except:
                                    print("re-message")
                                    continue


            # 코인베이스 상장 공시
            elif("코인베이스" in notice):
                if("launching" in notice):
                    # huobi
                    for coin in huobi_coinList:
                        if("/USDT" in coin):
                            coin_symbol = coin[:-5] # USDT를 빼기 심볼 자체만
                            
                            if(coin_symbol in notice):
                                seed = huobi.fetch_balance()["USDT"]["free"]

                                df = huobi.fetch_ohlcv(coin_symbol+str("/USDT"),"1m")
                                coin_current_price = df[-1][4] # 현재가
                                huobi.create_market_buy_order(coin_symbol+"/USDT",seed/coin_current_price*0.95)

                                # buybot
                                while(1):
                                    try:
                                        buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"(Huobi) "+str(coin)+" 코인베이스 상장 -> 매수하였습니다.")
                                        break
                                    except:
                                        print("re-message")
                                        continue


                    # upbit_Coin 
                    for coin in upbit_coinList: # 공지에 언급된 upbit코인이 있는지 확인
                        if(str(coin) in notice): # 공지에 코인이 언급되있을 경우 바로 매수
                            KRW_seed = upbit.get_balance("KRW")
                            upbit.buy_market_order("KRW-"+str(coin),KRW_seed*0.995)

                            # buybot
                            while(1):
                                try:
                                    buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"(Upbit) "+str(coin)+" 코인베이스 상장 -> 매수하였습니다.")
                                    break
                                except:
                                    print("re-message")
                                    continue

                    # upbit_Coin BTC
                    for coin in upbit_BTC_coinList: # 공지에 언급된 upbit코인이 있는지 확인
                        if(str(coin) in notice): # 공지에 코인이 언급되있을 경우
                            KRW_seed = upbit.get_balance("KRW")
                            upbit.buy_market_order("KRW-BTC",KRW_seed*0.995)
                            time.sleep(0.2)
                            BTC_seed = upbit.get_balance("KRW-BTC")
                            upbit.buy_market_order("BTC-"+str(coin),BTC_seed*0.994)
                
                            # buybot
                            while(1):
                                try:
                                    buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"(Upbit) "+str(coin)+" 코인베이스 상장 -> 매수하였습니다.")
                                    break
                                except:
                                    print("re-message")
                                    continue

                    # bithumb_Coin
                    for coin in bithumb_coinList:
                        if(str(coin) in notice):
                           
                            buy_count = 0

                            while(buy_count<3): # 총 3번 나누어 매수

                                buy_count+=1 

                                KRW_seed = bithumb.get_balance("BTC")[2] # 가지고있는 원화량

                                orderbook = pybithumb.get_orderbook(str(coin)) # 오더북
                                sell_price = orderbook['asks'][0]['price'] # 시장가 조회
                                unit = KRW_seed/float(sell_price)*0.70 # 살수 있는 물량

                                if(sell_price<100): # 코인가격이 100원 미만일 경우       100
                                    unit = int(unit/100)*100
                                    bithumb.buy_market_order(str(coin),unit)
                        
                                
                                elif(sell_price<1000): # 코인가격이 1000원 미만일 경우    10
                                    unit = int(unit/10)*10
                                    bithumb.buy_market_order(str(coin),unit)
                                    
                                elif(sell_price<10000): # 코인가격이 10000원 미만일 경우   1
                                    unit = int(unit)
                                    bithumb.buy_market_order(str(coin),unit)
                                    
                                elif(sell_price<100000): # 코인가격이 100000원 미만일 경우  0.1
                                    round_unit = round(unit,1) # 1까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.1)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        

                                elif(sell_price<1000000): # 코인가격이 1000000원 미만일 경우 0.01
                                    round_unit = round(unit,2) # 2까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.01)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        
                                elif(sell_price<10000000): # 코인가격이 10000000.....   0.001
                                    round_unit = round(unit,3) # 3까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.001)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                                        
                                else: # 코인가격이 10000000.....   0.0001
                                    round_unit = round(unit,4) # 4까지 반올림
                                    if(unit < round_unit): # 올림이 되었다는 의미므로
                                        bithumb.buy_market_order(str(coin),round_unit-0.0001)
                                        
                                    else: # 내림이 된것이므로 ok
                                        bithumb.buy_market_order(str(coin),round_unit)
                  
                            # buybot
                            while(1):
                                try:
                                    buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+notice+"\n"+"\n"+"(Bithumb) "+str(coin)+" 코인베이스 상장 -> 매수하였습니다.")
                                    break
                                except:
                                    print("re-message")
                                    continue
                    
            
            else: # 아무것도 아닐 경우
                while(1):
                    try:
                        bot.sendMessage(chat_id=id,text=str(datetime.datetime.now())+"\n"+"\n"+notice)
                        break
                    except:
                        print("re-message")
                        continue

            # case 3) 유의 공지
            # case 5) 업비트 NFT 선착순 이벤트

            time.sleep(1)

        if(current_notice!=notice): # 새로운 공지일 경우
            current_notice=notice

    except Exception as Ex:
        print("AWS_wallet ERROR")
        print(str(Ex))
        print(" ")

        time.sleep(1)
        
        while(1):
            try:
                bot.sendMessage(chat_id=id,text=str(datetime.datetime.now())+"\n"+"\n"+"ERROR  restart AWS_wallet")
                break
            except:
                print("re-message")
                continue

        while(1):
            try:
                buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+"ERROR  restart AWS_wallet"+"\n"+"\n"+"\n")
                break
            except:
                print("re-message")
                continue
        
        time.sleep(1)

        browser = webdriver.Chrome('크롬드라이버잇는 경로요', options=options)        

        continue
