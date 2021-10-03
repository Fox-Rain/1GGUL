# 추가할 것들....   1. 지갑이 여러개 닫혔을 경우 어느것을 매수할 것인지?   2. 타거래소 지갑감지 시스템
# ************* 픽스할것   주의  트위터가 새 트윗인지의 기준이 문장이 다른지만으로는 안됨... + 시간까지 다른지로 체크하도록 다시 설계해야함. (9/24)

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
import googletrans # 구글번역 Api

# beautiful Soup  user-agent
headers = {}

# API #

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

# 트위터 twitter Api
twit_consumer_key = 
twit_consumer_secret =
twit_access_token =
twit_access_token_secret=

auth = tweepy.OAuthHandler(twit_consumer_key,twit_consumer_secret)
auth.set_access_token(twit_access_token,twit_access_token_secret)

api = tweepy.API(auth)

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

# future binance (선물)(현물) Api
future_binance =
binance = 

# huobi Api
huobi = ccxt.huobipro()

# google trans Api
translator = googletrans.Translator()


# coin List #

# upbit coinList (BTC/KRW)
upbit_coinList = ["LTC","BCHA","ELF","GLM","BTT","ETC","ADA","DOGE","BTG","BSV","MTL","SRM","AXS","IOTA","SAND","STX","JST","FCT2","WAXP","KAVA","HIVE","FLOW","TRX","VET","EOS","DAWN","BCH","POWR","AQT","PLA","WAVES","QTUM","HBAR","CBK","OMG","TON","BORA","IOST","MLK","GAS","TRUEL","RFR","HUNT","ATOM","SNT","MED","NEO","UPP","MOC","PUNDIX","ONG","IQ","HUM","AHT","ORBS","SSX","STRAX","MANA","XEM","XTZ","STRK","REP","CVC","ICX","META","SXP","TT","LOOM","THETA","STEEM","ENJ","CHZ","ZIL","MVL","AERGO","SC","MBL","LSK","ARDR","CRE","STMX","SBD","ANKR","STORJ","DKA","LNC","ONT","POLY","QKC","GRS","MFT","ARK","STPT","BAT","ZRX","KNC","LINK"]
upbit_BTC_coinList = ["CELO","LRC","ONIT","FOR","RVN","FIL","BNT","SNX","LUNA","PSG","NKN","RLC","PROM","LINA","NMR","ALGO","DNT","INJ","CTSI","SUN","CHR","AUCTION","GO","GXC","NEAR","JUV","OXT","OGN","COMP","MKR","SOLVE","IOTX"]
upbit_BTC_wallet_coinList = ["MKR","COMP","NMR","PSG","AUCTION","UNI","PROM","JUV","INJ","SNX","NEAR","VAL","ALGO","CELO","BNT","RLC","CRV","PAX","DAI","HBD","OGN","GRT","FX","GXC","CTSI","LRC","NKN","OXT","CHR","BFC","DAD","DNT","ONIT","IOTX","FOR","DGB","LINA","RSR","SUN","GO","SOLVE"]

# bithumb  wallet_coinList
bithumb_wallet_coinList = ["LOOM","LF","BIOT","WEMIX","MSB","NU","UMA","ANV","VELO","ASM","ALICE","TEMCO","MM","VRA","MVC","WTC","DVI","SUN","SOC","REN","XNO","CELR","XPR","COS","YFI","BTG","HIVE","ELF","AWO","RLC","MANA","KNC","MLK","ORC","ADP","EL","ORBS","CAKE","LPT","FX","PUNDIX","BURGER","ZRX","MATIC","HDAC","GOM2","RSR","BORA","BFC","WAXP","PCI","KSM","QTCON","BOA","OXT","REP","FCT","QKC","CKB","BAL","GRT","TRV","BCD","CYCLUB","LRC","RINGX","UOS","MIR","CTXC","GHX","CENNZ","AAVE","NMR","MAP","XYM","OCEAN","RAI","AION","WOM","GXC","EVZ","HIBS","EM","MXC","DAD","VALOR","ARPA","FLETA","BNT","LINA","CHR","TRUE","APIX","COMP","CTSI","BEL","WIKEN","MKR","XVS","WOZX","DAI","BAKE","BLY","WICC","CTK","BAT"]
bithumb_coinList = bithumb.get_tickers() # 빗썸 전체 코인 가져옴

# binance future coinList
binance_future_coinList = ["1INCH/USDT","AAVE/USDT","ADA/USDT","AKRO/USDT","ALGO/USDT","ALICE/USDT","ALPHA/USDT","ANKR/USDT","ATOM/USDT","AVAX/USDT","AXS/USDT","BAKE/USDT","BAL/USDT","BAND/USDT","BAT/USDT","BCH/USDT","BEL/USDT","BLZ/USDT","BNB/USDT","BTS/USDT","BZRX/USDT","BTT/USDT","CELR/USDT","CHR/USDT","CHZ/USDT","COMP/USDT","COTI/USDT","CRV/USDT","CTK/USDT","CVC/USDT","DASH/USDT","DENT/USDT","DGB/USDT","DODO/USDT","DOGE/USDT","DOT/USDT","EGLD/USDT","ENJ/USDT","EOS/USDT","ETC/USDT","FIL/USDT","FLM/USDT","FTM/USDT","GRT/USDT","GTC/USDT","HBAR/USDT","HNT/USDT","HOT/USDT","ICP/USDT","ICX/USDT","IOST/USDT","IOTA/USDT","KAVA/USDT","KEEP/USDT","KNC/USDT","KSM/USDT","LINA/USDT","LINK/USDT","LIT/USDT","LRC/USDT","LTC/USDT","LUNA/USDT","MANA/USDT","MATIC/USDT","MKR/USDT","MTL/USDT","NEAR/USDT","NEO/USDT","NKN/USDT","OCEAN/USDT","OGN/USDT","OMG/USDT","ONE/USDT","ONT/USDT","QTUM/USDT","REEF/USDT","REN/USDT","RLC/USDT","RSR/USDT","RUNE/USDT","RVN/USDT","SAND/USDT","SFP/USDT","SKL/USDT","SNX/USDT","SOL/USDT","SRM/USDT","STMX/USDT","STORJ/USDT","SUSHI/USDT","SXP/USDT","THETA/USDT","TLM/USDT","TOMO/USDT","TRB/USDT","TRX/USDT","UNFI/USDT","UNI/USDT","VET/USDT","WAVES/USDT","XEM/USDT","XLM/USDT","XMR/USDT","XRP/USDT","XTZ/USDT","ZEC/USDT","ZEN/USDT","ZIL/USDT","ZRX/USDT"]
binance_coinList = binance.fetch_tickers() # 바이낸스 현물 코인 리스트

# huobi coinList
huobi_coinList = huobi.fetch_tickers() # 후오비 현물 코인


# influencer
influencer_List = ["BSC","Binance","짱펑_binance","Justin Sun","Elon Musk"]


# user agent
headers = {}

# FUCTION #

# 번역해주는 메소드
def google_Trans(twit):
    result = translator.translate(twit,dest='ko')
    return result


# 트윗닉넥임 -> 코인심볼로 바꾸어 리턴해주는 메소드
def twitname_To_Coin(twitname): # str(트윗명)을 파라미터로 받음  이후 코인의 심볼을 리턴함
    if("Verasity" in twitname):
        return "VRA"
    elif("Balancer" in twitname):
        return "BAL"
    elif("BioPassport" in twitname):
        return "BIOT"
    elif("MIXMARVEL" in twitname):
        return "MIX"
    elif("MISBLOC" in twitname):
        return "MSB"
    elif("Mirror" in twitname):
        return "MIR"
    elif("MXC" in twitname):
        return "MXC"
    elif("MAP" in twitname):
        return "MAP"
    elif("MileVerse" in twitname):
        return "MVC"
    elif("Alice" in twitname):
        return "ALICE"
    elif("LinkFlow" in twitname):
        return "LF"
    elif("Dvision" in twitname):
        return "DVI"
    elif("NuCypher" in twitname):
        return "NU"
    elif("Nestree" in twitname):
        return "EGG"
    elif("Nervos" in twitname):
        return "CKB"
    elif("GamerHash" in twitname):
        return "GHX"
    elif("Mina" in twitname):
        return "MINA"
    elif("Celsius" in twitname):
        return "CEL"
    elif("OMG" in twitname):
        return "OMG"
    elif("Sushi" in twitname):
        return "SUSHI"
    elif("Arweave" in twitname):
        return "AR"
    elif("Harmony" in twitname):
        return "ONE"
    elif("XinFin" in twitname):
        return "XDC"
    elif("Holo" in twitname):
        return "HOT"
    elif("Decred" in twitname):
        return "DCR"
    elif("THOR" in twitname):
        return "RUNE"
    elif("Dash" in twitname):
        return "DASH"
    elif("Helium" in twitname):
        return "HNT"
    elif("Kusama" in twitname): # 쿠사마 부터 다시 하드코딩... 트위터보고
        return "KSM"
    elif("Klaytn" in twitname):
        return "KLAY"
    elif("Fantom" in twitname):
        return "FTM"
    elif("Shib" in twitname):
        return "1000SHIB"
    elif("Monero" in twitname):
        return "XMR"
    elif("PancakeSwap" in twitname):
        return "CAKE"
    elif("DFINITY" in twitname):
        return "ICP"
    elif("Polygon" in twitname):
        return "MATIC"
    elif("Avalanche" in twitname):
        return "AVAX"
    elif("Orchid" in twitname):
        return "OXT"
    elif("Maker" in twitname):
        return "MKR"
    elif("Compound" in twitname):
        return "COMP"
    elif("district" in twitname):
        return"DNT"
    elif("Numerai" in twitname):
        return"NMR"
    elif("solve" in twitname):
        return"SOLVE"
    elif("iExec" in twitname):
        return"RLC"
    elif("DigiByte" in twitname):
        return"DGB"
    elif("DadChain" in twitname):
        return"DAD"
    elif("SUN" in twitname):
        return"SUN"
    elif("퀴즈톡" in twitname):
        return"QTCON"
    elif("Origin" in twitname):
        return"OGN"
    elif("Bancor" in twitname):
        return"BNT"
    elif("The Graph" in twitname):
        return"GRT"
    elif("GoChain" in twitname):
        return"GO"
    elif("Chromia" in twitname):
        return"CHR"
    elif("Uniswap" in twitname):
        return"UNI"
    elif("NKN" in twitname):
        return"NKN"
    elif("GXChain" in twitname):
        return"GXC"
    elif("IoTeX" in twitname):
        return"IOTX"
    elif("Reserve" in twitname):
        return"RSR"
    elif("Injective" in twitname):
        return"INJ"
    elif("Linear" in twitname):
        return"LINA"
    elif("TrueFi" in twitname):
        return" TUSD"
    elif("Maro" in twitname):
        return"MARO"
    elif("Prometeus" in twitname):
        return"PROM"
    elif("Celo" in twitname):
        return"CELO"
    elif("Function X" in twitname):
        return"FX"
    elif("Paxos" in twitname):
        return"PAX"
    elif("Paycoin" in twitname):
        return"PCI"
    elif("Loopring" in twitname):
        return"LRC"
    elif("Validity" in twitname):
        return"VAL"
    elif("Algorand" in twitname):
        return"ALGO"
    elif("NEAR" in twitname):
        return"NEAR"
    elif("Cartesi" in twitname):
        return"CTSI"
    elif("Synthetix" in twitname):
        return"SNX"
    elif("Raven" in twitname):
        return"RVN"
    elif("Terra" in twitname):
        return"LUNA"
    elif("BIFROST" in twitname):
        return"BFC"
    elif("Socios" in twitname):
        return "CHZ"
    elif("Protocol Labs" in twitname):
        return "FIL"
    elif("ONBUFF" in twitname):
        return "ONIT"
    elif("ForTube" in twitname):
        return "FOR"
    elif("Bounce" in twitname):
        return "AUCTION"
    elif("Standard Tokenization" in twitname):
        return "STPT"
    elif("Groesticoin" in twitname):
        return "GRS"
    elif("Basic Attention" in twitname):
        return "BAT"
    elif("Lisk" in twitname):
        return "LSK"
    elif("Refereum" in twitname):
        return "RFR"
    elif("Cobak" in twitname):
        return "CBK"
    elif("Thunder" in twitname):
        return "TT"
    elif("Loom" in twitname): # 룸네트워크 까지
        return "LOOM"        
    elif("GOLEM" in twitname):
        return "GLM"
    elif("아하" in twitname):
        return "AHT"
    elif("Storj" in twitname):
        return "STORJ"
    elif("Hifi" in twitname):
        return "MFT"
    elif("Ardor" in twitname):
        return "ARDR"
    elif("MovieBloc" in twitname):
        return "MBL"
    elif("0x" in twitname):
        return "ZRX"
    elif("Status" in twitname):
        return "SNT"
    elif("Augur" in twitname):
        return "REP"
    elif("Everipedia" in twitname):
        return "IQ"
    elif("Mossland" in twitname):
        return "MOC"
    elif("dKargo" in twitname):
        return "DKA"
    elif("Enjin" in twitname):
        return "ENJ"
    elif("Kyber Network" in twitname):
        return "KNC"
    elif("Quark" in twitname):
        return "QKC"
    elif("Ontology" in twitname):
        return "ONT"
    elif("StormX" in twitname):
        return "STMX"
    elif("Sia Foundation" in twitname):
        return "SC"
    elif("MVL" in twitname):
        return "MVL"
    elif("Uppsala" in twitname):
        return "UPP"
    elif("Strike" in twitname):
        return "STRK"
    elif("Zilliqa" in twitname):
        return "ZIL"
    elif("BORA" in twitname):
        return "BORA"
    elif("Ankr" in twitname):
        return "ANKR"
    elif("NEM" in twitname):
        return "XEM"
    elif("carryprotocol" in twitname):
        return "CRE"
    elif("FirmaChain" in twitname):
        return "FCT2"
    elif("Decentraland" in twitname):
        return "MANA"
    elif("Alpha Quark" in twitname):
        return "AQT"
    elif("Pundi X" in twitname):
        return "PUNDIX"
    elif("WAX" in twitname):
        return "WAXP"
    elif("Chiliz" in twitname):
        return "CHZ"
    elif("JUST" in twitname):
        return "JST"
    elif("Hive" in twitname):
        return "HIVE"
    elif("Tokamak Network" in twitname):
        return "TON"
    elif("Waves" in twitname):
        return "WAVES"
    elif("Stratis" in twitname):
        return "STRAX"
    elif("IOTA" in twitname):
        return "IOTA"
    elif("메타디움" in twitname):
        return "META"
    elif("stacks" in twitname):
        return "STX"
    elif("Civic" in twitname):
        return "CVC"
    elif("Aergo" in twitname):
        return "AERGO"
    elif("Neo" in twitname):
        return "NEO"
    elif("somesing" in twitname):
        return "SSX"
    elif("Dawn" in twitname):
        return "DAWN"
    elif("BitcoinCash" in twitname):
        return "BCH"
    elif("Orbs" in twitname):
        return "ORBS"
    elif("Powerledger" in twitname):
        return "POWR"
    elif("The Sandbox" in twitname):
        return "SAND"
    elif("Stellar" in twitname):
        return "XLM"
    elif("HUNT" in twitname):
        return "HUNT"
    elif("Bitcoin Gold" in twitname):
        return "BTG"
    elif("VeChain" in twitname):
        return "VET"
    elif("Polymath" in twitname):
        return "POLY"
    elif("Qtum" in twitname):
        return "QTUM"
    elif("MediBloc" in twitname):
        return "MED"
    elif("BitTorrent" in twitname):
        return "BTT"
    elif("Metal" in twitname):
        return "MTL"
    elif("Theta" in twitname):
        return "THETA"
    elif("Axie" in twitname):
        return "AXS"
    elif("Bitcoin SV" in twitname):
        return "BSV"
    elif("PlayDapp" in twitname):
        return "PLA"
    elif("Boba Network" in twitname):
        return "OMG"
    elif("Milk" in twitname):
        return "MLK"
    elif("elf" in twitname):
        return "ELF"
    elif("EOSIO" in twitname):
        return "EOS"
    elif("ICON" in twitname):
        return "ICX"
    elif("Doge" in twitname):
        return "DOGE"
    elif("Litecoin" in twitname):
        return "LTC"
    elif("ARK" in twitname):
        return "ARK"
    elif("steemit" in twitname):
        return "STEEM"
    elif("Ethereum Classic" in twitname):
        return "ETC"
    elif("TRON" in twitname):
        return "TRX"
    elif("Cosmos" in twitname):
        return "ATOM"
    elif("Cardano" in twitname):
        return "ADA"
    elif("Flow" in twitname):
        return "FLOW"
    elif("Tezos" in twitname):
        return "XTZ"
    elif("Serum" in twitname):
        return "SRM"
    elif("IOST" in twitname):
        return "IOST"
    elif("Hedera" in twitname):
        return "HBAR"
    elif("Bitcoin ABC" in twitname): # 여기까지 업비트 완료
        return "BCHA"
    elif("HABL" in twitname):
        return "HIBS"
    elif("FLETACHAIN" in twitname):
        return "FLETA"
    elif("TrueChain" in twitname):
        return "TRUE"
    elif("TrustVerse" in twitname):
        return "TRV"
    elif("TEMCO" in twitname):
        return "TEMCO"
    elif("Tachyon" in twitname):
        return "IPX"
    elif("Contentos" in twitname):
        return "COS"
    elif("Cortex Labs" in twitname):
        return "CTXC"
    elif("xenon" in twitname):
        return "XNO"
    elif("Eminer" in twitname):
        return "EM"
    elif("WEMIX" in twitname):
        return "WEMIX"
    elif("WaykiChain" in twitname):
        return "WICC"
    elif("WaltonChain" in twitname):
        return "WTC"
    elif("Ultra" in twitname):
        return "UOS"
    elif("UMA" in twitname):
        return "UMA"
    elif("WOM Protocol" in twitname):
        return "WOM"
    elif("Orbit Chain" in twitname):
        return "ORC"
    elif("Elysia" in twitname):
        return "EL"
    elif("RIZON" in twitname):
        return "HDAC"
    elif("ASSEMBLE" in twitname):
        return "ASM"
    elif("애니버스" in twitname):
        return "ANV"
    elif("ARPA" in twitname):
        return "ARPA"
    elif("APIS" in twitname):
        return "APIX"
    elif("Aion" in twitname):
        return "AION"
    elif("AMO" in twitname):
        return "AMO"
    elif("Certik Security" in twitname):
        return "CTK"
    elif("CelerNetwork" in twitname):
        return "CELR"
    elif("Centrality" in twitname):
        return "CENNZ"
    elif("Venus" in twitname):
        return "XVS"
    elif("BLOCERY" in twitname):
        return "BLY"
    elif("COTI" in twitname):
        return "COTI"
    elif("Ren" in twitname):
        return "REN"
    elif("Gala Games" in twitname):
        return "GALA"
    elif("FTX" in twitname):
        return "FTT"
    elif("dYdX" in twitname):
        return "DYDX"
    elif("The Kava Platform" in twitname):
        return "KAVA"
    elif("dForce" in twitname):
        return "DF"
    elif("Fetch" in twitname):
        return "FET"
    elif("Yield Guild Games" in twitname):
        return "YGG"
    elif("DODO DEX & NFT" in twitname):
        return "DODO"
    elif("Coin98 Wallet" in twitname):
        return "C98"
    elif("AlienWorlds" in twitname):
        return "TLM"
    elif("Mask Network" in twitname):
        return "MASK"
    elif("Electric Coin Company" in twitname):
        return "ZEC"
    elif("Oasis Foundation" in twitname):
        return "ROSE"
    elif("Conflux Network Official" in twitname):
        return "CFX"
    elif("Utrust" in twitname):
        return "UTK"
    elif("Audius" in twitname):
        return "AUDIO"
    elif("Automata Network" in twitname):
        return "ATA"
    elif("pNetwork" in twitname):
        return "PNT"
    elif("FUNToken.io" in twitname):
        return "FUN"
    elif("Raydium" in twitname):
        return "RAY"
    elif("TomoChain" in twitname):
        return "TOMO"
    elif("Trust Wallet" in twitname):
        return "TWT"
    elif("MOBOX" in twitname):
        return "MBOX"
    elif("Reef Finance" in twitname):
        return "REEF"
    elif("Litentry" in twitname):
        return "LIT"
    elif("Gitcoin" in twitname):
        return "GTC"
    elif("WazirX" in twitname):
        return "WRX"
    elif("Ellipsis" in twitname):
        return "EPS"
    elif("IDEX" in twitname):
        return "IDEX"
    elif("WINkLink" in twitname):
        return "WIN"
    elif("Toko Token" in twitname):
        return "TKO"
    elif("Vite Labs" in twitname):
        return "VITE"
    elif("Nano" in twitname):
        return "NANO"
    elif("Wanchain" in twitname):
        return "WAN"
    elif("bZx - Fulcrum" in twitname):
        return "BZRX"
    elif("autofarm.network" in twitname):
        return "AUTO"
    elif("Flamingo Finance" in twitname):
        return "FLM"
    elif("NULS" in twitname):
        return "NULS"
    elif("SuperFarm" in twitname):
        return "SUPER"
    elif("SKALE Network" in twitname):
        return "SKL"
    elif("Bluzelle" in twitname):
        return "BLZ"
    elif("Tellor" in twitname):
        return "TRB"
    elif("Clover Finance" in twitname):
        return "CLV"
    elif("adgerDAO" in twitname):
        return "BADGER"
    elif("BitShares News" in twitname):
        return "BTS"
    elif("Aragon" in twitname):
        return "ANT"
    elif("BarnBridg" in twitname):
        return "BOND"
    elif("Phala Network" in twitname):
        return "PHA"
    elif("DEGO" in twitname):
        return "DEGO"
    elif("DIA" in twitname):
        return "DIA"
    elif("Keep #tBTC" in twitname):
        return "KEEP"
    elif("Dusk Network" in twitname):
        return "DUSK"
    elif("Fei Labs" in twitname):
        return "TRIBE"
    elif("LTO Network" in twitname):
        return "LTO"
    elif("Streamr" in twitname):
        return "DATA"
    elif("Band Protocol" in twitname):
        return "BAND"                       # 대충 binanace 현물 10페이지까지의 코인들
    elif("Casper" in twitname):             # 여기서부터 huobi
        return "CSPR"    
    elif("MDEX" in twitname):
        return "MDX"    
    elif("Sperax" in twitname):
        return "SPA"    
    elif("Talken" in twitname):
        return "TALK"    
    elif("ZKSwap" in twitname):
        return "ZKS"    
    elif("Alchemy Pay" in twitname):
        return "ACH"    
    elif("Structure.finance" in twitname):
        return "STF"    
    elif("EMOGI" in twitname):
        return "LOL"    
    elif("DeFine" in twitname):
        return "DFA"    
    elif("Elastos" in twitname):
        return "ELA"    
    elif("EPIK Prime" in twitname):
        return "EPIK"    
    elif("Origo.Network" in twitname):
        return "OGO"    
    elif("PlatON" in twitname):
        return "LAT"    
    elif("Marlin" in twitname):
        return "POND"    
    elif("ArcBlock" in twitname):
        return "ABT"    
    elif("MASS" in twitname):
        return "MASS"    
    elif("BYTOM BLOCKCHAIN" in twitname):
        return "BTM"    
    elif("Project PAI" in twitname):
        return "PAI"    
    elif("Lambda" in twitname):
        return "LAMB"    
    elif("BruceYang_NEST" in twitname):
        return "NEST"    
    elif("WOO Network" in twitname):
        return "WOO"    
    elif("DATA" in twitname):
        return "DTA"    
    elif("TOP Network" in twitname):
        return "TOP"    
    elif("TNB Official" in twitname):
        return "TNB"    
    elif("AchainOfficial" in twitname):
        return "ACT"
    elif("FUSION" in twitname):
        return "FSN" 
    elif("Metaventurer" in twitname):
        return "YFII" 
    elif("Persistence" in twitname):
        return "XPRT" 
    elif("Ethereum Push Notification Service" in twitname):
        return "PUSH" 
    elif("CyberMiles" in twitname):
        return "CMT" 
    elif("Dock" in twitname):
        return "DOCK" 
    elif("IRIS Network" in twitname):
        return "IRIS" 
    elif("WhaleSharkdotPro" in twitname):
        return "WHALE" 
    elif("AirSwap" in twitname):
        return "AST" 
    elif("VidyCoin" in twitname):
        return "VIDY" 
    elif("Nebulas.io" in twitname):
        return "NAS" 
    elif("Request (REQ)" in twitname):
        return "REQ" 
    elif("Nexo" in twitname):
        return "NEXO" 
    elif("Firo" in twitname):
        return "FIRO" 
    elif("Nexus Mutual" in twitname):
        return "WNXM" 
    elif("U Network" in twitname):
        return "UUU" 
    elif("FansTime" in twitname):
        return "FTI" 
    elif("PowerPool" in twitname):
        return "CVP" 
    elif("Frontier" in twitname):
        return "FRONT" 
    elif("Value DeFi" in twitname):
        return "VALUE" 
    elif("FilDA" in twitname):
        return "FILDA" 
    elif("InsurAc" in twitname):
        return "INSUR" 
    elif("Robonomics" in twitname):
        return "XRT" 
    elif("xDai" in twitname):
        return "STAKE" 
    elif("API3" in twitname):
        return "API3" 
    

    else:
        return "None" # <--- None 


# 업비트 코인의 가격의 변화를 확인하는 메소드
def upbit_Coin_price_change(upbitcoin): # 파라미터로 코인명을 받음 + 변동률을 리턴함
    
    if(upbitcoin in upbit_coinList): # 코인이 만약 업비트/원화에 존재한다면
        df = pyupbit.get_ohlcv("KRW-"+str(upbitcoin), interval = "minute1")
        startprice = df["low"][-2] # 1분전 저가

        df = pyupbit.get_ohlcv("KRW-"+str(upbitcoin), interval = "minute1")
        endprice = df["close"][-1] # 현재가
        upbit_rate_change = (endprice-startprice)/startprice*100
        print(str(upbitcoin)+" "+str(upbit_rate_change))

        return round(upbit_rate_change,3) # 그 코인의 변동률을 리턴함

    else: # 업비트/원화 코인이 아니라면
        return 123


# 업비트 BTC 코인의 가격의 변화를 확인하는 메소드
def upbit_BTC_Coin_price_change(BTCupbitcoin):
    if(BTCupbitcoin in upbit_BTC_coinList):
        df = pyupbit.get_ohlcv("BTC-"+str(BTCupbitcoin), interval = "minute1")
        startprice = df["low"][-2] # 1분전 저가

        df = pyupbit.get_ohlcv("BTC-"+str(BTCupbitcoin), interval = "minute1")
        endprice = df["close"][-1] # 현재가
        upbit_BTC_rate_change = (endprice-startprice)/startprice*100
        print(str(BTCupbitcoin)+" "+str(upbit_BTC_rate_change))

        return round(upbit_BTC_rate_change,3)

    else: # 업비트 BTC 코인이 아니라면
        return 123

    
# 빗썸 코인의 가격의 변화를 확인하는 메소드
def bithumb_Coin_price_change(bithumbcoin):
    if(bithumbcoin in bithumb_coinList):
        df = bithumb.get_candlestick(str(bithumbcoin), chart_intervals="1m")
        startprice = df["low"][-2] # 1분전 저가

        df = bithumb.get_candlestick(str(bithumbcoin), chart_intervals="1m")
        endprice = df["close"][-1] # 현재가
        bithumb_rate_change = (endprice-startprice)/startprice*100
        print(str(bithumbcoin)+" "+str(bithumb_rate_change))

        return round(bithumb_rate_change,3)

    else: # 빗썸 코인이 아니라면
        return 123


# 바이낸스 현물 코인 가격의 변화를 확인하는 메소드
def binance_Coin_price_change(binance_coin):
    if(binance_coin+str("/USDT") in binance_coinList):
        df = binance.fetch_ohlcv(binance_coin+str("/USDT"),"1m")
        startprice = df[-2][3] # 1분전 저가

        df = binance.fetch_ohlcv(binance_coin+str("/USDT"),"1m")
        endprice = df[-1][4] # 현재가
        binance_rate_change = (endprice-startprice)/startprice*100
        print(str(binance_coin)+" "+str(binance_rate_change))

        return round(binance_rate_change,3)

    else: # 바이낸스 코인이 아니라면
        return 123


def huobi_Coin_price_chage(huobi_coin):
    if(huobi_coin+str("/USDT") in huobi_coinList):
        df = huobi.fetch_ohlcv(huobi_coin+str("/USDT"),"1m")
        startprice = df[-2][3] # 1분전 저가

        df = huobi.fetch_ohlcv(huobi_coin+str("/USDT"),"1m")
        endprice = df[-1][4] # 현재가
        huobi_rate_change = (endprice-startprice)/startprice*100
        print(str(huobi_coin)+" "+str(huobi_rate_change))

        return round(huobi_rate_change,3)
    
    else:
        return 123


# 바이낸스 선물 코인 가격의 변화를 확인하는 메소드
#def binance_future_Coin_price_change(binance_future_coin):


current_twit = None    # 최근 트윗


# 프로그램 첫 실행시 가장 최근의 트윗를 저장함

twit_check_time = time.time() # 트위터 api 제한때문에 트위터 크롤링한 시간을 저장하고 시간맞추어 실행시키기  1분마다 불러와서 이후 얼마나 상승인지 학인

twits = api.home_timeline(tweet_mode="extended") # 트위터 크롤링

current_twit = twits[0].full_text

print(twits[0].user.name)
print(current_twit)
print("-------------------------------------------------------------------------------------------------------")
print(" ")


while(1):

        # 트윗
    try:    
        time.sleep(0.2)

        if(time.time()>=twit_check_time+62): # 트윗을 불러온지 60초이상 지났을 경우
           
            print(time.time())

            twits = api.home_timeline(tweet_mode="extended")

            twit_check_time = time.time() # 크롤링한 시간을 다시 설정

            counting = 0 # 트위터 카운팅

            for i in range(0,19):
                if(twits[i].full_text == current_twit): # 최신트윗일 경우
                    break
                else:
                    counting+=1
            
            print(" ")
            print(counting)
            print(" ")

            if(counting!=0): # 카운팅이 0 이면 새로운 트윗이 없다는 의미므로 배제하고

                current_twit = twits[0].full_text # 다시 최근 트윗을 설정 

                time.sleep(5)
                for i in range(0,counting):
                    
                    # 거래소별 변동률을 저장할 변수들
                    upbit_rate = None
                    upbit_BTC_rate = None
                    bithumb_rate = None
                    binance_rate = None
                    huobi_rate = None

                    # 코인 존재 유무 플래그
                    upbit_flag = False
                    upbit_BTC_flag = False
                    bithumb_flag = False
                    binance_flag = False
                    huobi_flag = False

                    # 거래소별 메세지
                    upbit_message = "(Upbit)"
                    upbit_BTC_message = "(Upbit BTC)" 
                    bithumb_message = "(Bithumb)"
                    binance_message = "(Binance)"
                    huobi_message = "(Huobi)"

                    # 번역 성공유무 플래그
                    translate_Flag= False

                    print(twits[i].user.name)
                    print(twits[i].full_text)

                    print(" ")
                    print(" ")

                    coin_symbol = twitname_To_Coin(twits[i].user.name) # 트위터명을 코인심볼 / 인플루언서 로 변경

                    if(coin_symbol!="None"): # 트위터가 쓸모있는 트윗일 경우

                        # 코인일 경우  coin_symbol

                        rate_change_average = 0 # 거래소별 변동률의 평균을 저장할 변수
                        exchange_counting = 0 # 거래소개수

                        upbit_rate = upbit_Coin_price_change(str(coin_symbol)) # upbit 변동률을 리턴

                        if(upbit_rate==123): # 123이란것은 코인이 존재하지 않았다는 의미
                            upbit_rate = 0
                        else: # 거래소에 코인이 존재한다면
                            exchange_counting+=1
                            upbit_flag = True
                            
                        
                        upbit_BTC_rate = upbit_BTC_Coin_price_change(str(coin_symbol)) # upbit BTC 변동률을 리턴

                        if(upbit_BTC_rate==123):
                            upbit_BTC_rate = 0
                        else:
                            exchange_counting+=1
                            upbit_BTC_flag = True
                

                        bithumb_rate = bithumb_Coin_price_change(str(coin_symbol)) # bithumb 변동률을 리턴

                        if(bithumb_rate==123):
                            bithumb_rate = 0
                        else:
                            exchange_counting+=1
                            bithumb_flag = True


                        binance_rate = binance_Coin_price_change(str(coin_symbol)) # binance 변동률을 리턴

                        if(binance_rate==123):
                            binance_rate = 0
                        else:
                            exchange_counting+=1
                            binance_flag = True


                        huobi_rate = huobi_Coin_price_chage(str(coin_symbol)) # huobi 변동률 리턴

                        if(huobi_rate==123):
                            huobi_rate = 0
                        else:
                            exchange_counting+=1
                            huobi_flag = True


                        if(exchange_counting!=0): # 일단 코인이 존재하는 거래소가 1개 이상일 경우

                            rate_change_average = (upbit_rate+upbit_BTC_rate+bithumb_rate+binance_rate+huobi_rate)/exchange_counting # 거래소간 변동률의 평균


                            # 트윗내용 번역
                            Korean_twit = None
                            try:
                                Korean_twit = google_Trans(twits[i].full_text)
                                translate_Flag = True # 번역성공일 경우

                            except Exception as Ex:
                                print(str(Ex))


                            # 거래소별 매수하는 코드 # 거래소에 코인이 존재하지 않거나 존재하는 경우 2퍼이상 모든 거래소에서 상승이 일어나야만 호재로 판단하고 매수
                            if((upbit_flag==False or upbit_rate>2.2) and (upbit_BTC_flag==False or upbit_BTC_rate>2.5) and (bithumb_flag==False or bithumb_rate>2.2) and (binance_flag==False or binance_rate>2) and (huobi_flag==False or huobi_rate>2.2)): # 평균적으로 2.3퍼이상의 상승을 보였을 경우 매수를 실행

                                if(upbit_flag==True): # 업비트에 코인이 존재할 경우 매수
                                    KRW_seed = upbit.get_balance("KRW")
                                    upbit.buy_market_order("KRW-"+str(coin_symbol),KRW_seed*0.995)

                                    upbit_message = "(Upbit) Rate change is "+str(upbit_rate)+"\n"+"매수하였습니다."
                                
                                if(upbit_BTC_flag==True): # 업비트 BTC 존재할 경우 매수
                                    KRW_seed = upbit.get_balance("KRW")
                                    upbit.buy_market_order("KRW-BTC",KRW_seed*0.995)
                                    time.sleep(0.2)
                                    BTC_seed = upbit.get_balance("KRW-BTC")
                                    upbit.buy_market_order("BTC-"+str(coin_symbol),BTC_seed*0.994)

                                    upbit_BTC_message = "(Upbit BTC) Rate change is "+str(upbit_BTC_rate)+"\n"+"매수하였습니다."

                                if(bithumb_flag==True): # 빗썸 매수
                                    
                                    buy_count = 0

                                    while(buy_count<3): # 총 3번 나누어 매수

                                        buy_count+=1 

                                        KRW_seed = bithumb.get_balance("BTC")[2] # 가지고있는 원화량

                                        orderbook = pybithumb.get_orderbook(str(coin_symbol)) # 오더북
                                        sell_price = orderbook['asks'][0]['price'] # 시장가 조회
                                        unit = KRW_seed/float(sell_price)*0.70 # 살수 있는 물량

                                        if(sell_price<100): # 코인가격이 100원 미만일 경우       100
                                            unit = int(unit/100)*100
                                            bithumb.buy_market_order(str(coin_symbol),unit)
                                
                                        
                                        elif(sell_price<1000): # 코인가격이 1000원 미만일 경우    10
                                            unit = int(unit/10)*10
                                            bithumb.buy_market_order(str(coin_symbol),unit)
                                            
                                        elif(sell_price<10000): # 코인가격이 10000원 미만일 경우   1
                                            unit = int(unit)
                                            bithumb.buy_market_order(str(coin_symbol),unit)
                                            
                                        elif(sell_price<100000): # 코인가격이 100000원 미만일 경우  0.1
                                            round_unit = round(unit,1) # 1까지 반올림
                                            if(unit < round_unit): # 올림이 되었다는 의미므로
                                                bithumb.buy_market_order(str(coin_symbol),round_unit-0.1)
                                                
                                            else: # 내림이 된것이므로 ok
                                                bithumb.buy_market_order(str(coin_symbol),round_unit)
                                                

                                        elif(sell_price<1000000): # 코인가격이 1000000원 미만일 경우 0.01
                                            round_unit = round(unit,2) # 2까지 반올림
                                            if(unit < round_unit): # 올림이 되었다는 의미므로
                                                bithumb.buy_market_order(str(coin_symbol),round_unit-0.01)
                                                
                                            else: # 내림이 된것이므로 ok
                                                bithumb.buy_market_order(str(coin_symbol),round_unit)
                                                
                                        elif(sell_price<10000000): # 코인가격이 10000000.....   0.001
                                            round_unit = round(unit,3) # 3까지 반올림
                                            if(unit < round_unit): # 올림이 되었다는 의미므로
                                                bithumb.buy_market_order(str(coin_symbol),round_unit-0.001)
                                                
                                            else: # 내림이 된것이므로 ok
                                                bithumb.buy_market_order(str(coin_symbol),round_unit)
                                                
                                        else: # 코인가격이 10000000.....   0.0001
                                            round_unit = round(unit,4) # 4까지 반올림
                                            if(unit < round_unit): # 올림이 되었다는 의미므로
                                                bithumb.buy_market_order(str(coin_symbol),round_unit-0.0001)
                                                
                                            else: # 내림이 된것이므로 ok
                                                bithumb.buy_market_order(str(coin_symbol),round_unit)

                                    bithumb_message = "(Bithumb) Rate change is "+str(bithumb_rate)+"\n"+"매수하였습니다."

                                if(binance_flag==True): # 바이낸스 매수
                                    seed = binance.fetch_balance()["USDT"]['free']

                                    df = binance.fetch_ohlcv(coin_symbol+str("/USDT"),"1m")
                                    coin_current_price = df[-1][4] # 현재가

                                    binance.create_market_buy_order(coin_symbol+"/USDT",seed/coin_current_price*0.95)

                                    binance_message = "(Binance) Rate change is "+str(binance_rate)+"\n"+"매수하였습니다."
                                
                                if(huobi_flag==True): # 후오비 매수
                                    seed = huobi.fetch_balance()["USDT"]["free"]

                                    df = huobi.fetch_ohlcv(coin_symbol+str("/USDT"),"1m")
                                    coin_current_price = df[-1][4] # 현재가

                                    huobi.create_market_buy_order(coin_symbol+"/USDT",seed/coin_current_price*0.95)

                                    huobi_message = "(Huobi) Rate change is "+str(huobi_rate)+"\n"+"매수하였습니다."


                                # 트위터 내용을 BinanceBuyBot으로 보냄
                                if(translate_Flag == True): # 번역에 성공했을 경우
                                    while(1):
                                        try:
                                            buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+ "   "+str(coin_symbol)+"   "+"\n"+"\n"+twits[i].full_text+"\n"+"\n"+"\n"+"(번역)"+"\n"+Korean_twit.text+"\n"+"\n"+"\n"+"\n"+"\n"+"\"Exchange Average Rate\"  "+str(round(rate_change_average,3))+"\n"+"\n"+"\n"+upbit_message+"\n"+"\n"+upbit_BTC_message+"\n"+"\n"+bithumb_message+"\n"+"\n"+binance_message+"\n"+"\n"+huobi_message)        
                                            break
                                        except:
                                            print("re-message3")
                                            continue
                                
                                if(translate_Flag == False): # 번역 실패했을 경우
                                    while(1):
                                        try:
                                            buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+"   "+ str(coin_symbol)+"   "+"\n"+"\n"+twits[i].full_text+"\n"+"\n"+"\n"+"\n"+"\n"+"\"Exchange Average Rate\"  "+str(round(rate_change_average,3))+"\n"+"\n"+"\n"+upbit_message+"\n"+"\n"+upbit_BTC_message+"\n"+"\n"+bithumb_message+"\n"+"\n"+binance_message+"\n"+"\n"+huobi_message)        
                                            break
                                        except:
                                            print("re-message4")
                                            continue

                            else: # 상승률이 2.3퍼 미만일 경우

                                if(upbit_flag==True):
                                    upbit_message = "(Upbit) Rate change is "+str(upbit_rate)+"\n"+"호재로 판단되지않아 매수하지 않았습니다."

                                if(upbit_BTC_flag==True):
                                    upbit_BTC_message = "(Upbit BTC) Rate change is "+str(upbit_BTC_rate)+"\n"+"호재로 판단되지않아 매수하지 않았습니다."

                                if(bithumb_flag==True):
                                    bithumb_message = "(Bithumb) Rate change is "+str(bithumb_rate)+"\n"+"호재로 판단되지않아 매수하지 않았습니다."
                                
                                if(binance_flag==True):
                                    binance_message = "(Binance) Rate change is "+str(binance_rate)+"\n"+"호재로 판단되지않아 매수하지 않았습니다."

                                if(huobi_flag==True):
                                    huobi_message = "(Huobi) Rate change is "+str(huobi_rate)+"\n"+"호재로 판단되지않아 매수하지 않았습니다."

                                # 트위터 내용을 BinanceBot으로 보냄
                                if(translate_Flag == True): # 번역에 성공했을 경우
                                    while(1):
                                        try:
                                            bot.sendMessage(chat_id=id,text=str(datetime.datetime.now())+"\n"+"\n"+"   "+ str(coin_symbol)+"   "+"\n"+"\n"+twits[i].full_text+"\n"+"\n"+"\n"+"(번역)"+"\n"+Korean_twit.text+"\n"+"\n"+"\n"+"\n"+"\n"+"\"Exchange Average Rate\"  "+str(round(rate_change_average,3))+"\n"+"\n"+"\n"+upbit_message+"\n"+"\n"+upbit_BTC_message+"\n"+"\n"+bithumb_message+"\n"+"\n"+binance_message+"\n"+"\n"+huobi_message)        
                                            break
                                        except:
                                            print("re-message3")
                                            continue
                                
                                if(translate_Flag == False): # 번역 실패했을 경우
                                    while(1):
                                        try:
                                            bot.sendMessage(chat_id=id,text=str(datetime.datetime.now())+"\n"+"\n"+"   "+ str(coin_symbol)+"   "+"\n"+"\n"+twits[i].full_text+"\n"+"\n"+"\n"+"\n"+"\n"+"\"Exchange Average Rate\"  "+str(round(rate_change_average,3))+"\n"+"\n"+"\n"+upbit_message+"\n"+"\n"+upbit_BTC_message+"\n"+"\n"+bithumb_message+"\n"+"\n"+binance_message+"\n"+"\n"+huobi_message)        
                                            break
                                        except:
                                            print("re-message4")
                                            continue
                        


                        time.sleep(1)
            
            else: # 새트윗이 없을때
                print("None....")
            time.sleep(0.5)

            # 추가 예정 거래소
            # binance_Coin  (FUTURE/...)
            # huobi_Coin
            # gateio_Coin ...
    
    except Exception as EX:
        print(str(EX)+"\n"+"  AWS_twit ERROR")
        time.sleep(1)

        while(1):
            try:
                bot.sendMessage(chat_id=id,text=str(datetime.datetime.now())+"\n"+"\n"+"ERROR  restart AWS_twit")
                break
            except:
                print("re-message")
                continue
        
        while(1):
            try:
                buy_bot.sendMessage(chat_id=id2,text=str(datetime.datetime.now())+"\n"+"\n"+"ERROR  restart AWS_twit"+"\n"+"\n"+"\n")
                break
            except:
                print("re-message")
                continue

        
        while(1):
            try:
                twits = api.home_timeline(tweet_mode="extended") # 트위터 크롤링
                break
            except:
                continue

        time.sleep(3)

        twit_check_time = time.time() # 트위터 api 제한때문에 트위터 크롤링한 시간을 저장하고 시간맞추어 실행시키기  1분마다 불러와서 이후 얼마나 상승인지 학인

        current_twit = twits[0].full_text

        continue
        
    



     
