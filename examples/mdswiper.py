from simplekivy import SimpleKivy
s = SimpleKivy(title="swiper", md_mode=True)

links = {"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.fMBitZbrgt9tutQZ96TCzQHaEK%26pid%3DApi&f=1&ipt=01ac1a3edda2cf194ce1ad1143a7253ed46295f3cd990ada3a084456f68aae63&ipo=images",
        "https://i.pinimg.com/474x/69/72/a0/6972a0241165d427f62dbc57d09d2feb--naru-barakamon-faithful.jpg",
        "https://alien9.crossrealms.net/pictures/screenshots/episode-1/alien-nine-episode-1-3.jpg"}

swiper = s.MDSwiper()

for link in links:
    swiperitem = s.MDSwiperItem() 
    s.build({swiperitem:s.FitImage(source=link, radius=[30]),
     swiper:swiperitem})
    
s + [
    [swiper]
]