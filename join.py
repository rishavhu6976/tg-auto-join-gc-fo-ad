import asyncio
from pyrogram import Client
from pyrogram.errors import (
    UserAlreadyParticipant, InviteHashExpired,
    InviteHashInvalid, FloodWait, ChannelsTooMuch,
    PeerFlood, ChatAdminRequired, UserBannedInChannel
)

# === CONFIG ===
API_ID = 123456          # From my.telegram.org
API_HASH = "your_api_hash"
SESSION_NAME = "joiner_session"
DELAY_BETWEEN_JOINS = 4  # seconds (increase if you get flood errors)

# === FULL GROUP LIST ===
RAW_LINKS = """
https://t.me/+XW3IzOXiwDo3MTFl
https://t.me/+fmIiCJonBqoxNTY9
https://t.me/+iVezbwvLzLY5YTM1
https://t.me/+scyO01uu5NljZTU1
https://t.me/+xxlG89hQchNhYWE1
https://t.me/ABESCROWTEAM
https://t.me/ABUPDATECHAT
https://t.me/AEC_ALCoders
https://t.me/AH_CHAT
https://t.me/AIMGODCHATGROUP
https://t.me/AIMGODRESELLINGHUB
https://t.me/ALI_CHAT_GC
https://t.me/ALONZOxRESELLERS
https://t.me/ALPHASTORE20
https://t.me/AlienxSaverchat
https://t.me/AN0NYMOUS_CHAT
https://t.me/ANGELSUPDATE1
https://t.me/ANITOOLSGC
https://t.me/Ansariclone
https://t.me/APEXCHATGROUP
https://t.me/APKHUB_GROUP_2
https://t.me/aspirestudymca
https://t.me/astenchatbro
https://t.me/AVINASHESCROW
https://t.me/Awais_CloudsBuyAndSell
https://t.me/AzTechGC
https://t.me/AzTechsGC
https://t.me/B4CHATZONE
https://t.me/BESTXSOMCHAT
https://t.me/BGMIGROUPCHAT01
https://t.me/BGMIIDSELLBZARRR
https://t.me/BGMIPOP002
https://t.me/BGMIPOP333
https://t.me/BGMI_C0MMUNITY
https://t.me/BGMIxGROUPx2
https://t.me/BIGBOSSCHATGROUPa
https://t.me/Bihar_2024
https://t.me/BijinderGroupTalks
https://t.me/BLACKY_TALKS
https://t.me/BlackHatsssss
https://t.me/BR0WSEANDSEARCH
https://t.me/Brutodworld
https://t.me/BUYSALEOFFICIALL
https://t.me/BuySell_TGs
https://t.me/Buy_Sell_RusRek_New_York
https://t.me/Buyselllgc
https://t.me/BuzzCZ
https://t.me/BuzzChatGroup
https://t.me/CARDER_MAXX_ESCROW
https://t.me/CamprunCommunity
https://t.me/CamprunCommunity1
https://t.me/capricornmart
https://t.me/cashbackadaa
https://t.me/CHATON24H
https://t.me/CHAT_DARKS
https://t.me/CHAT_ZONE2
https://t.me/CharixChat
https://t.me/CharixGlobalChat
https://t.me/ChaseChats
https://t.me/charthub01
https://t.me/chatbindass
https://t.me/chatspar
https://t.me/chatting_hub_u
https://t.me/chesswar_group
https://t.me/CLASHOFCLANS_SELL_BUY
https://t.me/CLASH_OF_CLANS_BUY_AND_SELLING
https://t.me/Clash_of_clans_sell_buy
https://t.me/clashermarket3
https://t.me/CLogyShopGc
https://t.me/coachayomidelegitupdate
https://t.me/COD_DEALS
https://t.me/coc_sell_buy_account
https://t.me/cocbsbuysell
https://t.me/comchating
https://t.me/COMMUNITYPOWERS
https://t.me/CosmicAdsGroup
https://t.me/cracking_Web
https://t.me/cryptocashguy
https://t.me/Cuet_mca
https://t.me/CYBERCRIMECOMMUNITY
https://t.me/cybertrustvault
https://t.me/DAMAN_OFFICIAL_HUB
https://t.me/DARK_BLZRED_EXE
https://t.me/dailyearning4478
https://t.me/Darkboyupdates
https://t.me/data_science9
https://t.me/data_science_group
https://t.me/datascience32
https://t.me/dealatpeak
https://t.me/dealzhubstar
https://t.me/deathchatting_world
https://t.me/DEMONGENZGC
https://t.me/DevilModsFeedback1
https://t.me/discuss_group
https://t.me/dollarxescrowservice
https://t.me/dostologgarh
https://t.me/DragoSellingZone
https://t.me/DREAM2EARNN
https://t.me/DRACO_RESELLERS
https://t.me/DYNAMOCHATGROUPOP
https://t.me/DYNAMOxESCROWS
https://t.me/DabangEscrow
https://t.me/eagleescrowsir
https://t.me/earnchatgroup
https://t.me/EARNING_NEWS_CHATS
https://t.me/earningchat1
https://t.me/earningzq
https://t.me/ELDORADOCOMMUNITY
https://t.me/elite_resellers
https://t.me/elitechatss
https://t.me/EMM_international
https://t.me/empire_chatz
https://t.me/EncChats
https://t.me/Envy_Chats
https://t.me/Epic_Loot_Club_02
https://t.me/eraofdealer
https://t.me/Escrow_Deals
https://t.me/Escrow_E
https://t.me/Etb_Online_Marketing
https://t.me/EVOS_ESCROW_SERVICE
https://t.me/everythingxottmarket
https://t.me/EXCELLENTxCHATHUB
https://t.me/FAITHFULL_HUB_TALK
https://t.me/FALCONRESSELINGSHOP
https://t.me/ff_id_seller_buyer
https://t.me/fflikegroups
https://t.me/fileworkalso
https://t.me/FLASH_X_CHATS
https://t.me/for_links123
https://t.me/freeccchecker9
https://t.me/freefirechattinggroup24
https://t.me/FreeFireRedeemCodecommunity
https://t.me/Free_Fire_Indian_Group
https://t.me/FreeNetflixbuying
https://t.me/Free_promotion_19
https://t.me/FreePromotionGroup3
https://t.me/freekamal19
https://t.me/freepromotionall11
https://t.me/freupdatechatgroup
https://t.me/FREEFIRETOURNAMENTALL
https://t.me/FIRE_X_LIVE_FEEDBACK
https://t.me/Fsproviderchat
https://t.me/ftsbitcoin
https://t.me/fyh7u
https://t.me/GANDHI_ESCROW_SERVICE
https://t.me/gamingmarket2
https://t.me/GC_CHAT7
https://t.me/geminigalaxy
https://t.me/GENUINE_UPI_BOTZ_CHATS
https://t.me/Giveawaybykks
https://t.me/Glitchwa
https://t.me/GMDyadhu
https://t.me/GMRWWaknO
https://t.me/GNFmodschat
https://t.me/Goku_Officials
https://t.me/gold365_skyexchange_99exch
https://t.me/googlepayearninga
https://t.me/googlereview000
https://t.me/googletaskjobs
https://t.me/Groupsmallrobig
https://t.me/guardianescrow0
https://t.me/gvlootmyntra
https://t.me/hacker3073
https://t.me/HackerDisscussion
https://t.me/HARSHLOOTER0
https://t.me/harsh_er4_chat
https://t.me/HARYANASYSTUMM
https://t.me/help_eachother_990
https://t.me/hephzi444
https://t.me/HeroxResellers
https://t.me/hindi_english_chatting_group_pro
https://t.me/hindi_english_chatting_group_zon
https://t.me/Humics
https://t.me/HUNTER_MOD_X_CHAT
https://t.me/HydraChatsGroup
https://t.me/httpstmedn6JUHsHzUw5Yjc6
https://t.me/ibbustore
https://t.me/IDAO652
https://t.me/IbrahimDiscussion
https://t.me/ijhdzsa
https://t.me/IGCCXSTAR
https://t.me/immortalescrow
https://t.me/incomeacadamy
https://t.me/INDANEHPGASBOOKING5
https://t.me/indchatpvt
https://t.me/IndianGamingMarketOfficial
https://t.me/indian_otp_group_gmail_sell_buy
https://t.me/indianotphub
https://t.me/indianotpseller022
https://t.me/INFOSCAM34
https://t.me/infofather8
https://t.me/Itz_venom_family
https://t.me/itzdhruvbiochat
https://t.me/itzdhruvfreindsgroup
https://t.me/itzlifafa
https://t.me/itzteamlegendchat
https://t.me/JAATXONWER
https://t.me/JACKIExPOPSELLING
https://t.me/jalwagamevipif
https://t.me/jannatfile
https://t.me/jarviskagroup
https://t.me/jbehhfhhrbfujd
https://t.me/jeremygroupchat
https://t.me/jezzy_market
https://t.me/jiomart_super
https://t.me/jiomartx
https://t.me/joensush
https://t.me/JORDANxESCROW
https://t.me/JoyceCasho
https://t.me/KACHRASTOREGROUP
https://t.me/KALKIESCROWSERVICE
https://t.me/KALKIxMARKET
https://t.me/k7dff
https://t.me/kartikchat17
https://t.me/KelidenUpdatesChats
https://t.me/killernxtchat
https://t.me/KOIPAYmm001
https://t.me/kri4i4i4i4
https://t.me/KSHITIJESCROWSERVICE
https://t.me/kukaoft
https://t.me/kushrahoachaearnkaro
https://t.me/LB_Movies
https://t.me/latenitedrop
https://t.me/legitupdatewithcoachayomide
https://t.me/LFBuyerAndSeller
https://t.me/lfmarlfb
https://t.me/Lifafa_Loot_dalo
https://t.me/lokeshgamer00007
https://t.me/lookingfrsmthng
https://t.me/lootdeals144
https://t.me/LOBBYKENAWAB
https://t.me/LORDMETHODSCHAT
https://t.me/LUCIFERxRESELLERSHUB
https://t.me/Luciferxtalkk
https://t.me/LUXURYWORLDCHATZONE
https://t.me/m4wynxarsiv
https://t.me/magicbullet_600
https://t.me/makemoneyonline023
https://t.me/makemoneyonline1434
https://t.me/mantuearning009
https://t.me/marinefordopbr
https://t.me/metaearth02
https://t.me/milliondollarminds
https://t.me/mimitvupdatediscussiongroup
https://t.me/missionnimcet2
https://t.me/mlmbusinessPromotion
https://t.me/moneymakers4h
https://t.me/moneymakingspree
https://t.me/money_transfer_work_agent
https://t.me/MOMOCHATS
https://t.me/mrperfectvip000_chat
https://t.me/mrvinirxgroup
https://t.me/Mr_C4RLO_GC
https://t.me/MSGT2
https://t.me/MTEARNERZ
https://t.me/MUTHALQT
https://t.me/mxnshuchat
https://t.me/My_tg_family
https://t.me/na2kl
https://t.me/NAIJAHUBPAY
https://t.me/nairapay_payout
https://t.me/NAWAB_RESELLING
https://t.me/Nawabresellercommunity
https://t.me/ndiskco
https://t.me/netflixtvactivationchat
https://t.me/NIMCETG
https://t.me/NIMCET_discussion_group
https://t.me/niluda
https://t.me/nimcet2026aspirantt
https://t.me/nimcet_2026_group
https://t.me/nimcetodisha
https://t.me/nimcettarget2
https://t.me/nimcetzone
https://t.me/NineMarketPlace
https://t.me/nisshuuuuu
https://t.me/no_investment_work_01
https://t.me/NobleEscrow
https://t.me/nutnest
https://t.me/nyxisland
https://t.me/odiadealhub
https://t.me/OFMgrind
https://t.me/official_tradevest
https://t.me/Official_free_earn_chat
https://t.me/oflznk
https://t.me/OG_BADBUNNYX
https://t.me/ogbadbunny
https://t.me/OmegaRishuFam
https://t.me/onlinemarketingstar
https://t.me/onlinefinders
https://t.me/OnlineDealsAndOffers2021
https://t.me/onlyfunandmasti
https://t.me/OPAYXCASHchat
https://t.me/OPxFFCHAT
https://t.me/OPxOTPChat
https://t.me/OpInsaneStoreChatGroup
https://t.me/OpxAliDiscussion
https://t.me/Otp_Group_ReChudi
https://t.me/otp_sellers_CyberAayan
https://t.me/otp_sellers_indian
https://t.me/otphub_group
https://t.me/page_marketplace_IG
https://t.me/paidmodchat
https://t.me/paidmodchatting
https://t.me/paidmodeescrow
https://t.me/paidmodffreeprediction
https://t.me/PalaceErotic
https://t.me/PANNEL_100
https://t.me/paulupdates
https://t.me/PayoutReal
https://t.me/peruzalen
https://t.me/pokemon_forever69
https://t.me/POPIDMARKET
https://t.me/PopXStore
https://t.me/powercheatgroup
https://t.me/PRIMEBGMI
https://t.me/PRINCEWORKK
https://t.me/PROGAMERMODSOFC
https://t.me/profiterzchat
https://t.me/proxhacker_backup
https://t.me/PROMOTE_ADDA
https://t.me/promotiongroupindia
https://t.me/plugersmarket
https://t.me/plugversegc
https://t.me/PVT_METHOD_CHAT
https://t.me/pushkarsgc
https://t.me/pythonalgodiscussion
https://t.me/quychat
https://t.me/R0YAL_WORLD
https://t.me/RAIDENRESELLERSHUB
https://t.me/RAKURAICHATGROUP1
https://t.me/RANGERxCOMMUNITY
https://t.me/rayygrp
https://t.me/RDX_CHAT
https://t.me/realchatgroups
https://t.me/redoxresellergroup
https://t.me/redzonechatgroup
https://t.me/Reemskumar1
https://t.me/REFERANDEARN1433
https://t.me/RefForRefGrup
https://t.me/Ref_Exchange_With_Hezekiel
https://t.me/ResetGc
https://t.me/Reseller_AtBGMI
https://t.me/RESELLERCHATGROUPS
https://t.me/RESELLERHUBX
https://t.me/RESELLERSADDAA
https://t.me/RESELLERS_CHAT_GROUP_BGMI
https://t.me/RESELLER_COMUNITY
https://t.me/RESELLING_STUFF
https://t.me/Resellers_Group
https://t.me/RESLLERSHR
https://t.me/RESSELERCOMUNITY
https://t.me/reviewappwork
https://t.me/REXXY_TEAM
https://t.me/Rishiotpgroup
https://t.me/RITESHxRESELLING
https://t.me/RIZZLERSELLINGZONE
https://t.me/rizxiterz
https://t.me/ROHANMODERFEEDBACK
https://t.me/ROWDYRESELLINGHUB
https://t.me/Royal_clashers_MarkeT
https://t.me/rpkagc
https://t.me/RupeesEscrowS
https://t.me/SAKKYHUBCHAT
https://t.me/SAMKIGC
https://t.me/SAND_FEEDBACK
https://t.me/sarkar_army_1
https://t.me/sateliteamitkr115
https://t.me/ScammerHellGroup
https://t.me/ScammersAlert_CHAT
https://t.me/securedmarts
https://t.me/Secrets_pro_chat
https://t.me/sell9Q
https://t.me/sell_and_buy7
https://t.me/sellchod
https://t.me/SELLIING_GC
https://t.me/seller_ws_group1
https://t.me/SellezzHub
https://t.me/sellerskidukkan
https://t.me/SellingZone51
https://t.me/sellingatpeak
https://t.me/sellinghub883
https://t.me/sellingmarket2
https://t.me/SeyiUpdateChat
https://t.me/SharkMarkets
https://t.me/Sharmajigroop
https://t.me/SheildEscrow
https://t.me/SHOPPIE_CHATS
https://t.me/SHARP_RESELLERS
https://t.me/SidraEscrowServices
https://t.me/Sikkim_Tashanwin_Prediction
https://t.me/skyforce07
https://t.me/SNIPER_BHAI_CHATS
https://t.me/SOHILRESELLERSCOMMUNITY
https://t.me/SoulBrutalBackup
https://t.me/Soul_Escrow
https://t.me/spam_free_links
https://t.me/SPHXLabsChat
https://t.me/spreadinggyansub4sub123
https://t.me/StarsUpdate_ChatRoom
https://t.me/star_update_chatroom
https://t.me/sti_world
https://t.me/STRONGBGMISTORECHAT
https://t.me/SUFIYANxRESELLER
https://t.me/SUJITRESELLERHUB
https://t.me/SukunaUpdate
https://t.me/SumitGiveawaysChat
https://t.me/swiggyno1mod
https://t.me/TANMOYMODX_CHEAT_GRUOP
https://t.me/Taptapcombos_chat
https://t.me/TARGETNIMCET_2023
https://t.me/taskagent150
https://t.me/talkworlds
https://t.me/tamilanDiscussion
https://t.me/tdgroup_5
https://t.me/TDNBACKUP
https://t.me/TEAM17CHAT
https://t.me/teambot_chats
https://t.me/TechBaseXChat
https://t.me/TechError
https://t.me/techtitans2025
https://t.me/techyabhiiii
https://t.me/TellerUsdtChat
https://t.me/TenkaiGods
https://t.me/text_gc
https://t.me/textique
https://t.me/TexTins
https://t.me/TGTECHOTP
https://t.me/THE_MAJOROPGROUP
https://t.me/TheChatGc
https://t.me/theunknownlooterz
https://t.me/tmaxgc
https://t.me/To_Mateix
https://t.me/ton_pay_community
https://t.me/TradingSquareDiscussionGroupadm
https://t.me/trading2030
https://t.me/TRIPPYCHAT70
https://t.me/tridentnetworking
https://t.me/TrustefiedMarket
https://t.me/trustgroupchat
https://t.me/TrustifySupport
https://t.me/ttiirkR0PWbpiZWQ1
https://t.me/TuneUpAcademy
https://t.me/UPDATEGROUP111
https://t.me/UNIH0
https://t.me/UNIQUE_EARNER
https://t.me/unholymarket
https://t.me/updatehubgroup
https://t.me/updateishere
https://t.me/updatezone72
https://t.me/UPI_UNIVERSE_CHAT
https://t.me/usdtindiasbuyandsell
https://t.me/VANSHCHATGROUP
https://t.me/varshagroupzen
https://t.me/VarienBgmiChat
https://t.me/vanhdzsssios
https://t.me/VenusDroid
https://t.me/verifiedbootz
https://t.me/verifiedonlineupdates
https://t.me/VerifiedExcrowGroup
https://t.me/VeriTrustEscrowOnTop
https://t.me/VICHARxSHABHA
https://t.me/vikshomecumhere
https://t.me/VIPHACKERSGUILD
https://t.me/vsv_coders
https://t.me/VYNCcoinChat
https://t.me/walkdrovenumbers
https://t.me/WARZ_CHAT
https://t.me/WHATSAPPFILE1212
https://t.me/WHATSAPWORKERS
https://t.me/WHITE_MONEY_ZONE_0
https://t.me/wienerdogequestions
https://t.me/WienerDogeonSol
https://t.me/winrow
https://t.me/WORLDBIGDEAL
https://t.me/WorldOtpGc
https://t.me/WS_CHAT_2008
https://t.me/WS_GOATS_01
https://t.me/wsfamily0
https://t.me/wsfaster1010
https://t.me/wsgroupforall
https://t.me/x7teamchat
https://t.me/x7teamotp
https://t.me/xdcheatchat
https://t.me/xorazm_chata_galdost
https://t.me/xyuzhsi
https://t.me/YTRESELLERSCOMMUNITY
https://t.me/yuimbro
https://t.me/ZAINCHATGROUP
https://t.me/zashchat
https://t.me/Zobto_market
https://t.me/ZodGc
https://t.me/Zruxnfchat
https://t.me/zwypaminechat
https://t.me/ZYNOX_CHEATS_786
https://t.me/adult_worker
https://t.me/aheer00
https://t.me/allinworldchat
https://t.me/annex_gc
https://t.me/apkOpc
https://t.me/avatarsells
https://t.me/aztechs_hub
https://t.me/best_friends_chatting_grp0
https://t.me/bettungbyharshit
https://t.me/bgmipop45
https://t.me/bgmipopgc99
https://t.me/bgmipopularity17
https://t.me/bin_generatorr
https://t.me/boostxad
https://t.me/botpaycommunity
https://t.me/bro1market
https://t.me/bullescrownetwork
https://t.me/burpyopchat
https://t.me/buyandsellbytruzd
https://t.me/buyingandsellinghere
https://t.me/buyingsellingnf
https://t.me/ChatxGcc
https://t.me/ChatzGc
https://t.me/CodeCrusherz
https://t.me/Cricketbuzz_Cricbet99_reddy_anna
https://t.me/globelchat
https://t.me/gmailbuyerseller1
https://t.me/gojo_igcc_talks
https://t.me/jaaniresellers
https://t.me/jackingsell
https://t.me/OldGroupMart
"""

def parse_links(raw):
    seen = set()
    links = []
    for line in raw.strip().splitlines():
        link = line.strip()
        if link.startswith("https://t.me/") and link not in seen:
            seen.add(link)
            links.append(link)
    return links

async def join_group(client, link):
    try:
        if "/+" in link:
            hash_part = link.split("/+")[-1]
            await client.join_chat(hash_part)
        else:
            username = link.rstrip("/").split("/")[-1]
            await client.join_chat(username)
        return "joined"
    except UserAlreadyParticipant:
        return "already_in"
    except (InviteHashExpired, InviteHashInvalid):
        return "invalid_link"
    except ChannelsTooMuch:
        return "too_many_channels"
    except UserBannedInChannel:
        return "banned"
    except PeerFlood:
        print("  ⚠️  PeerFlood! Sleeping 60s...")
        await asyncio.sleep(60)
        return "peer_flood"
    except FloodWait as e:
        print(f"  ⏳ FloodWait {e.value}s, sleeping...")
        await asyncio.sleep(e.value + 2)
        return "flood_waited"
    except Exception as ex:
        return f"error: {type(ex).__name__}: {ex}"

async def main():
    GROUPS = parse_links(RAW_LINKS)
    total = len(GROUPS)

    results = {
        "joined": [],
        "already_in": [],
        "invalid_link": [],
        "too_many_channels": [],
        "banned": [],
        "peer_flood": [],
        "flood_waited": [],
        "error": [],
    }

    async with Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH) as app:
        me = await app.get_me()
        print(f"\n{'='*50}")
        print(f"  🤖 Logged in as: {me.first_name} (@{me.username})")
        print(f"  📋 Total groups to process: {total}")
        print(f"{'='*50}\n")

        for i, link in enumerate(GROUPS, 1):
            short = link.replace("https://t.me/", "@")
            print(f"[{i:>3}/{total}] {short[:45]:<45}", end=" → ", flush=True)

            status = await join_group(app, link)
            print(status)

            # Categorize
            if status in results:
                results[status].append(link)
            elif status.startswith("error"):
                results["error"].append(f"{link}  ({status})")

            # Stop if account hit group limit
            if status == "too_many_channels":
                print("\n❌ Account has reached max group limit! Stopping.")
                break

            await asyncio.sleep(DELAY_BETWEEN_JOINS)

    # ── SUMMARY ──────────────────────────────────────
    print(f"\n{'='*50}")
    print("           📊  FINAL SUMMARY")
    print(f"{'='*50}")
    print(f"  ✅  Newly joined      : {len(results['joined'])}")
    print(f"  👤  Already in        : {len(results['already_in'])}")
    print(f"  🔗  Invalid/expired   : {len(results['invalid_link'])}")
    print(f"  🚫  Banned            : {len(results['banned'])}")
    print(f"  ⚠️   Peer flood hit    : {len(results['peer_flood'])}")
    print(f"  ⏳  Flood waited      : {len(results['flood_waited'])}")
    print(f"  ❌  Errors            : {len(results['error'])}")
    print(f"  📦  Group limit hit   : {len(results['too_many_channels'])}")
    processed = sum(len(v) for v in results.values())
    print(f"{'─'*50}")
    print(f"  📌  Total processed   : {processed} / {total}")
    print(f"{'='*50}\n")

    if results["error"]:
        print("🔍 Error details:")
        for e in results["error"]:
            print(f"   {e}")

if __name__ == "__main__":
    asyncio.run(main())
