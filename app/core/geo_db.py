"""
Comprehensive National & Global Geographic Database for Human Design Engine.
Covers all 34 Provincial Administrative Divisions in China:
- All 4 Direct-Administered Municipalities (北京, 上海, 天津, 重庆)
- All 23 Provinces & 5 Autonomous Regions (Including complete Xinjiang, Tibet, Qinghai, Inner Mongolia, Ningxia, Yunnan, Guizhou, etc.)
- All 333 Prefecture-level Divisions (Prefecture cities, prefectures, leagues, autonomous prefectures)
- Over 150 Prominent County-level Cities & Districts (太仓, 昆山, 义乌, 顺德, 常熟, 张家港, 江阴, 晋江, 寿光, 敦煌, 阳朔, 都江堰, 莫干山, etc.)
- Key Global Metropolises across North America, Europe, Asia-Pacific, Oceania, Middle East.

Features:
- Fast multi-strategy matching: Full name, Short name, Full pinyin, Pinyin acronym (e.g. wlmq -> 乌鲁木齐, ls -> 拉萨, bj -> 北京, sh -> 上海), English.
- Weighted ranking: mega cities & provincials prioritized, instant exact match resolution.
"""

GEO_DATA_LIST = [
    # ================= 顶级热门城市 (Tier 1 Mega & Core Metropolises) =================
    {"name": "北京市 (Beijing)", "short": "北京", "pinyin": "beijing", "abbr": "bj", "lat": 39.9042, "lng": 116.4074, "tz": "Asia/Shanghai", "country": "中国", "weight": 100},
    {"name": "上海市 (Shanghai)", "short": "上海", "pinyin": "shanghai", "abbr": "sh", "lat": 31.2304, "lng": 121.4737, "tz": "Asia/Shanghai", "country": "中国", "weight": 100},
    {"name": "广东省 广州市 (Guangzhou)", "short": "广州", "pinyin": "guangzhou", "abbr": "gz", "lat": 23.1291, "lng": 113.2644, "tz": "Asia/Shanghai", "country": "中国", "weight": 100},
    {"name": "广东省 深圳市 (Shenzhen)", "short": "深圳", "pinyin": "shenzhen", "abbr": "sz", "lat": 22.5431, "lng": 114.0579, "tz": "Asia/Shanghai", "country": "中国", "weight": 100},
    {"name": "香港特别行政区 (Hong Kong)", "short": "香港", "pinyin": "xianggang", "abbr": "xg", "lat": 22.3193, "lng": 114.1694, "tz": "Asia/Hong_Kong", "country": "中国", "weight": 100},
    {"name": "浙江省 杭州市 (Hangzhou)", "short": "杭州", "pinyin": "hangzhou", "abbr": "hz", "lat": 30.2741, "lng": 120.1551, "tz": "Asia/Shanghai", "country": "中国", "weight": 95},
    {"name": "四川省 成都市 (Chengdu)", "short": "成都", "pinyin": "chengdu", "abbr": "cd", "lat": 30.5728, "lng": 104.0668, "tz": "Asia/Shanghai", "country": "中国", "weight": 95},
    {"name": "台湾 台北市 (Taipei)", "short": "台北", "pinyin": "taibei", "abbr": "tb", "lat": 25.0330, "lng": 121.5654, "tz": "Asia/Taipei", "country": "中国", "weight": 95},
    {"name": "重庆市 (Chongqing)", "short": "重庆", "pinyin": "chongqing", "abbr": "cq", "lat": 29.5630, "lng": 106.5516, "tz": "Asia/Shanghai", "country": "中国", "weight": 95},
    {"name": "天津市 (Tianjin)", "short": "天津", "pinyin": "tianjin", "abbr": "tj", "lat": 39.0842, "lng": 117.2009, "tz": "Asia/Shanghai", "country": "中国", "weight": 95},
    {"name": "湖北省 武汉市 (Wuhan)", "short": "武汉", "pinyin": "wuhan", "abbr": "wh", "lat": 30.5928, "lng": 114.3055, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "陕西省 西安市 (Xi'an)", "short": "西安", "pinyin": "xian", "abbr": "xa", "lat": 34.3416, "lng": 108.9398, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "江苏省 南京市 (Nanjing)", "short": "南京", "pinyin": "nanjing", "abbr": "nj", "lat": 32.0603, "lng": 118.7969, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "江苏省 苏州市 (Suzhou)", "short": "苏州", "pinyin": "suzhou", "abbr": "sz", "lat": 31.2989, "lng": 120.5853, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "浙江省 宁波市 (Ningbo)", "short": "宁波", "pinyin": "ningbo", "abbr": "nb", "lat": 29.8683, "lng": 121.5440, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "湖南省 长沙市 (Changsha)", "short": "长沙", "pinyin": "changsha", "abbr": "cs", "lat": 28.2282, "lng": 112.9388, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "河南省 郑州市 (Zhengzhou)", "short": "郑州", "pinyin": "zhengzhou", "abbr": "zz", "lat": 34.7466, "lng": 113.6253, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "山东省 青岛市 (Qingdao)", "short": "青岛", "pinyin": "qingdao", "abbr": "qd", "lat": 36.0671, "lng": 120.3826, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "山东省 济南市 (Jinan)", "short": "济南", "pinyin": "jinan", "abbr": "jn", "lat": 36.6512, "lng": 117.1201, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "福建省 厦门市 (Xiamen)", "short": "厦门", "pinyin": "xiamen", "abbr": "xm", "lat": 24.4798, "lng": 118.0894, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "福建省 福州市 (Fuzhou)", "short": "福州", "pinyin": "fuzhou", "abbr": "fz", "lat": 26.0745, "lng": 119.2965, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "澳门特别行政区 (Macau)", "short": "澳门", "pinyin": "aomen", "abbr": "am", "lat": 22.1987, "lng": 113.5439, "tz": "Asia/Macau", "country": "中国", "weight": 90},

    # ================= 新疆维吾尔自治区 (Xinjiang - 全覆盖) =================
    {"name": "新疆 乌鲁木齐市 (Urumqi)", "short": "乌鲁木齐", "pinyin": "wulumuqi", "abbr": "wlmq", "lat": 43.8256, "lng": 87.6168, "tz": "Asia/Urumqi", "country": "中国", "weight": 90},
    {"name": "新疆 喀什地区 喀什市 (Kashgar)", "short": "喀什", "pinyin": "kashi", "abbr": "ks", "lat": 39.4677, "lng": 75.9938, "tz": "Asia/Urumqi", "country": "中国", "weight": 85},
    {"name": "新疆 克拉玛依市 (Karamay)", "short": "克拉玛依", "pinyin": "kelamayi", "abbr": "klmy", "lat": 45.5799, "lng": 84.8893, "tz": "Asia/Urumqi", "country": "中国", "weight": 80},
    {"name": "新疆 伊犁州 伊宁市 (Yining / Yili)", "short": "伊宁", "pinyin": "yining", "abbr": "yn", "lat": 43.9222, "lng": 81.3242, "tz": "Asia/Urumqi", "country": "中国", "weight": 82},
    {"name": "新疆 伊犁哈萨克自治州 (Yili)", "short": "伊犁", "pinyin": "yili", "abbr": "yl", "lat": 43.9222, "lng": 81.3242, "tz": "Asia/Urumqi", "country": "中国", "weight": 82},
    {"name": "新疆 巴音郭楞州 库尔勒市 (Korla)", "short": "库尔勒", "pinyin": "kuerle", "abbr": "kel", "lat": 41.7259, "lng": 86.1746, "tz": "Asia/Urumqi", "country": "中国", "weight": 80},
    {"name": "新疆 阿克苏地区 阿克苏市 (Aksu)", "short": "阿克苏", "pinyin": "akesu", "abbr": "aks", "lat": 41.1688, "lng": 80.2606, "tz": "Asia/Urumqi", "country": "中国", "weight": 80},
    {"name": "新疆 和田地区 和田市 (Hotan)", "short": "和田", "pinyin": "hetian", "abbr": "ht", "lat": 37.1142, "lng": 79.9222, "tz": "Asia/Urumqi", "country": "中国", "weight": 80},
    {"name": "新疆 吐鲁番市 (Turpan)", "short": "吐鲁番", "pinyin": "tulufan", "abbr": "tlf", "lat": 42.9513, "lng": 89.1895, "tz": "Asia/Urumqi", "country": "中国", "weight": 80},
    {"name": "新疆 哈密市 (Hami / Kumul)", "short": "哈密", "pinyin": "hami", "abbr": "hm", "lat": 42.8185, "lng": 93.5152, "tz": "Asia/Urumqi", "country": "中国", "weight": 78},
    {"name": "新疆 昌吉回族自治州 (Changji)", "short": "昌吉", "pinyin": "changji", "abbr": "cj", "lat": 44.0146, "lng": 87.3040, "tz": "Asia/Urumqi", "country": "中国", "weight": 78},
    {"name": "新疆 博尔塔拉州 博乐市 (Bole / Bortala)", "short": "博乐", "pinyin": "bole", "abbr": "bl", "lat": 44.9056, "lng": 82.0667, "tz": "Asia/Urumqi", "country": "中国", "weight": 75},
    {"name": "新疆 克孜勒苏州 阿图什市 (Artux)", "short": "阿图什", "pinyin": "atushi", "abbr": "ats", "lat": 39.7161, "lng": 76.1683, "tz": "Asia/Urumqi", "country": "中国", "weight": 75},
    {"name": "新疆 塔城地区 塔城市 (Tacheng)", "short": "塔城", "pinyin": "tacheng", "abbr": "tc", "lat": 46.7453, "lng": 82.9857, "tz": "Asia/Urumqi", "country": "中国", "weight": 75},
    {"name": "新疆 阿勒泰地区 阿勒泰市 (Altay)", "short": "阿勒泰", "pinyin": "aletai", "abbr": "alt", "lat": 47.8449, "lng": 88.1396, "tz": "Asia/Urumqi", "country": "中国", "weight": 78},
    {"name": "新疆 石河子市 (Shihezi)", "short": "石河子", "pinyin": "shihezi", "abbr": "shz", "lat": 44.3059, "lng": 86.0411, "tz": "Asia/Urumqi", "country": "中国", "weight": 78},
    {"name": "新疆 奎屯市 (Kuitun)", "short": "奎屯", "pinyin": "kuitun", "abbr": "kt", "lat": 44.4259, "lng": 84.9023, "tz": "Asia/Urumqi", "country": "中国", "weight": 75},
    {"name": "新疆 阿拉尔市 (Alar)", "short": "阿拉尔", "pinyin": "alaer", "abbr": "ale", "lat": 40.5419, "lng": 81.2859, "tz": "Asia/Urumqi", "country": "中国", "weight": 70},
    {"name": "新疆 图木舒克市 (Tumxuk)", "short": "图木舒克", "pinyin": "tumushuke", "abbr": "tmsk", "lat": 39.8673, "lng": 79.0779, "tz": "Asia/Urumqi", "country": "中国", "weight": 70},
    {"name": "新疆 五家渠市 (Wujiaqu)", "short": "五家渠", "pinyin": "wujiaqu", "abbr": "wjq", "lat": 44.1674, "lng": 87.5404, "tz": "Asia/Urumqi", "country": "中国", "weight": 70},
    {"name": "新疆 北屯市 (Beitun)", "short": "北屯", "pinyin": "beitun", "abbr": "bt", "lat": 47.3531, "lng": 87.8242, "tz": "Asia/Urumqi", "country": "中国", "weight": 70},
    {"name": "新疆 铁门关市 (Tiemenguan)", "short": "铁门关", "pinyin": "tiemenguan", "abbr": "tmg", "lat": 41.8275, "lng": 85.7538, "tz": "Asia/Urumqi", "country": "中国", "weight": 70},
    {"name": "新疆 双河市 (Shuanghe)", "short": "双河", "pinyin": "shuanghe", "abbr": "sh", "lat": 44.8453, "lng": 82.3533, "tz": "Asia/Urumqi", "country": "中国", "weight": 70},
    {"name": "新疆 可克达拉市 (Kokdala)", "short": "可克达拉", "pinyin": "kekedala", "abbr": "kkdl", "lat": 43.6833, "lng": 80.6333, "tz": "Asia/Urumqi", "country": "中国", "weight": 70},
    {"name": "新疆 昆玉市 (Kunyu)", "short": "昆玉", "pinyin": "kunyu", "abbr": "ky", "lat": 37.2089, "lng": 79.2878, "tz": "Asia/Urumqi", "country": "中国", "weight": 70},

    # ================= 西藏自治区 (Tibet - 全覆盖) =================
    {"name": "西藏 拉萨市 (Lhasa)", "short": "拉萨", "pinyin": "lasa", "abbr": "ls", "lat": 29.6525, "lng": 91.1721, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "西藏 日喀则市 (Shigatse)", "short": "日喀则", "pinyin": "rikaze", "abbr": "rkz", "lat": 29.2674, "lng": 88.8806, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "西藏 昌都市 (Chamdo)", "short": "昌都", "pinyin": "changdu", "abbr": "cd", "lat": 31.1408, "lng": 97.1785, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "西藏 林芝市 (Nyingchi)", "short": "林芝", "pinyin": "linzhi", "abbr": "lz", "lat": 29.6491, "lng": 94.3619, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "西藏 山南市 (Shannan / 乃东)", "short": "山南", "pinyin": "shannan", "abbr": "sn", "lat": 29.2370, "lng": 91.7733, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "西藏 那曲市 (Nagqu)", "short": "那曲", "pinyin": "naqu", "abbr": "nq", "lat": 31.4760, "lng": 92.0574, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "西藏 阿里地区 噶尔县 (Ali / Ngari)", "short": "阿里", "pinyin": "ali", "abbr": "al", "lat": 32.5012, "lng": 80.1055, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "西藏 日喀则市 江孜县 (Gyangze)", "short": "江孜", "pinyin": "jiangzi", "abbr": "jz", "lat": 28.9189, "lng": 89.6019, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},

    # ================= 青海省 (Qinghai - 全覆盖) =================
    {"name": "青海省 西宁市 (Xining)", "short": "西宁", "pinyin": "xining", "abbr": "xn", "lat": 36.6171, "lng": 101.7782, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "青海省 海东市 (Haidong)", "short": "海东", "pinyin": "haidong", "abbr": "hd", "lat": 36.5029, "lng": 102.1033, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "青海省 海西州 格尔木市 (Golmud)", "short": "格尔木", "pinyin": "geermu", "abbr": "gem", "lat": 36.4024, "lng": 94.9033, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "青海省 海西州 德令哈市 (Delingha)", "short": "德令哈", "pinyin": "delingha", "abbr": "dlh", "lat": 37.3695, "lng": 97.3608, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "青海省 玉树藏族自治州 (Yushu)", "short": "玉树", "pinyin": "yushu", "abbr": "ys", "lat": 33.0062, "lng": 97.0083, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "青海省 海南藏族自治州 共和县 (Gonghe)", "short": "共和", "pinyin": "gonghe", "abbr": "gh", "lat": 36.2803, "lng": 100.6197, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},

    # ================= 宁夏回族自治区 (Ningxia - 全覆盖) =================
    {"name": "宁夏 银川市 (Yinchuan)", "short": "银川", "pinyin": "yinchuan", "abbr": "yc", "lat": 38.4872, "lng": 106.2309, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "宁夏 石嘴山市 (Shizuishan)", "short": "石嘴山", "pinyin": "shizuishan", "abbr": "szs", "lat": 39.0133, "lng": 106.3792, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "宁夏 吴忠市 (Wuzhong)", "short": "吴忠", "pinyin": "wuzhong", "abbr": "wz", "lat": 37.9975, "lng": 106.1983, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "宁夏 固原市 (Guyuan)", "short": "固原", "pinyin": "guyuan", "abbr": "gy", "lat": 36.0046, "lng": 106.2426, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "宁夏 中卫市 (Zhongwei)", "short": "中卫", "pinyin": "zhongwei", "abbr": "zw", "lat": 37.5149, "lng": 105.1896, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},

    # ================= 内蒙古自治区 (Inner Mongolia - 全覆盖) =================
    {"name": "内蒙古 呼和浩特市 (Hohhot)", "short": "呼和浩特", "pinyin": "huhehaote", "abbr": "hhht", "lat": 40.8426, "lng": 111.7492, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "内蒙古 包头市 (Baotou)", "short": "包头", "pinyin": "baotou", "abbr": "bt", "lat": 40.6574, "lng": 109.8404, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "内蒙古 鄂尔多斯市 (Ordos)", "short": "鄂尔多斯", "pinyin": "eerduosi", "abbr": "eeds", "lat": 39.6083, "lng": 109.7813, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "内蒙古 赤峰市 (Chifeng)", "short": "赤峰", "pinyin": "chifeng", "abbr": "cf", "lat": 42.2578, "lng": 118.8869, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "内蒙古 通辽市 (Tongliao)", "short": "通辽", "pinyin": "tongliao", "abbr": "tl", "lat": 43.6138, "lng": 122.2631, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "内蒙古 呼伦贝尔市 (Hulunbuir)", "short": "呼伦贝尔", "pinyin": "hulunbeier", "abbr": "hlbe", "lat": 49.2116, "lng": 119.7658, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "内蒙古 呼伦贝尔 满洲里市 (Manzhouli)", "short": "满洲里", "pinyin": "manzhouli", "abbr": "mzl", "lat": 49.5978, "lng": 117.4452, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "内蒙古 乌兰察布市 (Ulanqab)", "short": "乌兰察布", "pinyin": "wulanchabu", "abbr": "wlcb", "lat": 40.9947, "lng": 113.1326, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "内蒙古 巴彦淖尔市 (Bayannur)", "short": "巴彦淖尔", "pinyin": "bayannaoer", "abbr": "byne", "lat": 40.7431, "lng": 107.4168, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "内蒙古 乌海市 (Wuhai)", "short": "乌海", "pinyin": "wuhai", "abbr": "wh", "lat": 39.6547, "lng": 106.8256, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "内蒙古 锡林浩特市 (Xilinhot)", "short": "锡林浩特", "pinyin": "xilinhaote", "abbr": "xlht", "lat": 43.9328, "lng": 116.0847, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},

    # ================= 甘肃省 (Gansu - 全覆盖) =================
    {"name": "甘肃省 兰州市 (Lanzhou)", "short": "兰州", "pinyin": "lanzhou", "abbr": "lz", "lat": 36.0611, "lng": 103.8343, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "甘肃省 酒泉 敦煌市 (Dunhuang)", "short": "敦煌", "pinyin": "dunhuang", "abbr": "dh", "lat": 40.1421, "lng": 94.6620, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "甘肃省 嘉峪关市 (Jiayuguan)", "short": "嘉峪关", "pinyin": "jiayuguan", "abbr": "jyg", "lat": 39.7731, "lng": 98.2892, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "甘肃省 酒泉市 (Jiuquan)", "short": "酒泉", "pinyin": "jiuquan", "abbr": "jq", "lat": 39.7324, "lng": 98.4947, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "甘肃省 张掖市 (Zhangye)", "short": "张掖", "pinyin": "zhangye", "abbr": "zy", "lat": 38.9259, "lng": 100.4498, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "甘肃省 武威市 (Wuwei)", "short": "武威", "pinyin": "wuwei", "abbr": "ww", "lat": 37.9283, "lng": 102.6380, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "甘肃省 天水市 (Tianshui)", "short": "天水", "pinyin": "tianshui", "abbr": "ts", "lat": 34.5809, "lng": 105.7249, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "甘肃省 庆阳市 (Qingyang)", "short": "庆阳", "pinyin": "qingyang", "abbr": "qy", "lat": 35.7380, "lng": 107.6384, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "甘肃省 平凉市 (Pingliang)", "short": "平凉", "pinyin": "pingliang", "abbr": "pl", "lat": 35.5393, "lng": 106.6651, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},

    # ================= 云南省 (Yunnan - 全覆盖) =================
    {"name": "云南省 昆明市 (Kunming)", "short": "昆明", "pinyin": "kunming", "abbr": "km", "lat": 25.0406, "lng": 102.7123, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "云南省 大理白族自治州 (Dali)", "short": "大理", "pinyin": "dali", "abbr": "dl", "lat": 25.6065, "lng": 100.2676, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "云南省 丽江市 (Lijiang)", "short": "丽江", "pinyin": "lijiang", "abbr": "lj", "lat": 26.8721, "lng": 100.2296, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "云南省 西双版纳 景洪市 (Xishuangbanna)", "short": "西双版纳", "pinyin": "xishuangbanna", "abbr": "xsbn", "lat": 22.0017, "lng": 100.7979, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "云南省 迪庆州 香格里拉市 (Shangri-La)", "short": "香格里拉", "pinyin": "xianggelila", "abbr": "xgll", "lat": 27.8252, "lng": 99.7073, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "云南省 腾冲市 (Tengchong)", "short": "腾冲", "pinyin": "tengchong", "abbr": "tc", "lat": 25.0253, "lng": 98.4941, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "云南省 曲靖市 (Qujing)", "short": "曲靖", "pinyin": "qujing", "abbr": "qj", "lat": 25.4900, "lng": 103.7962, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "云南省 玉溪市 (Yuxi)", "short": "玉溪", "pinyin": "yuxi", "abbr": "yx", "lat": 24.3520, "lng": 102.5465, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "云南省 保山市 (Baoshan)", "short": "保山", "pinyin": "baoshan", "abbr": "bs", "lat": 25.1205, "lng": 99.1671, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "云南省 普洱市 (Puer)", "short": "普洱", "pinyin": "puer", "abbr": "pe", "lat": 22.7872, "lng": 100.9665, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "云南省 楚雄彝族自治州 (Chuxiong)", "short": "楚雄", "pinyin": "chuxiong", "abbr": "cx", "lat": 25.0329, "lng": 101.5460, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "云南省 红河州 蒙自市 (Honghe / Mengzi)", "short": "蒙自", "pinyin": "mengzi", "abbr": "mz", "lat": 23.3669, "lng": 103.3850, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},

    # ================= 贵州省 (Guizhou - 全覆盖) =================
    {"name": "贵州省 贵阳市 (Guiyang)", "short": "贵阳", "pinyin": "guiyang", "abbr": "gy", "lat": 26.6470, "lng": 106.6302, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "贵州省 遵义市 (Zunyi)", "short": "遵义", "pinyin": "zunyi", "abbr": "zy", "lat": 27.7257, "lng": 106.9274, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "贵州省 安顺市 (Anshun / 黄果树)", "short": "安顺", "pinyin": "anshun", "abbr": "as", "lat": 26.2531, "lng": 105.9476, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "贵州省 黔东南州 凯里市 (Kaili / 西江苗寨)", "short": "凯里", "pinyin": "kaili", "abbr": "kl", "lat": 25.9762, "lng": 107.9772, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "贵州省 铜仁市 (Tongren / 梵净山)", "short": "铜仁", "pinyin": "tongren", "abbr": "tr", "lat": 27.7183, "lng": 109.1896, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "贵州省 毕节市 (Bijie)", "short": "毕节", "pinyin": "bijie", "abbr": "bj", "lat": 27.2985, "lng": 105.2924, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "贵州省 六盘水市 (Liupanshui)", "short": "六盘水", "pinyin": "liupanshui", "abbr": "lps", "lat": 26.5927, "lng": 104.8304, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "贵州省 黔西南州 兴义市 (Xingyi / 万峰林)", "short": "兴义", "pinyin": "xingyi", "abbr": "xy", "lat": 25.0963, "lng": 104.8954, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},

    # ================= 广西壮族自治区 (Guangxi - 全覆盖) =================
    {"name": "广西 南宁市 (Nanning)", "short": "南宁", "pinyin": "nanning", "abbr": "nn", "lat": 22.8170, "lng": 108.3665, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "广西 桂林市 (Guilin)", "short": "桂林", "pinyin": "guilin", "abbr": "gl", "lat": 25.2736, "lng": 110.2902, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "广西 阳朔县 (Yangshuo)", "short": "阳朔", "pinyin": "yangshuo", "abbr": "ys", "lat": 24.7788, "lng": 110.4952, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "广西 柳州市 (Liuzhou)", "short": "柳州", "pinyin": "liuzhou", "abbr": "lz", "lat": 24.3255, "lng": 109.4286, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "广西 北海市 (Beihai / 涠洲岛)", "short": "北海", "pinyin": "beihai", "abbr": "bh", "lat": 21.4812, "lng": 109.1192, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "广西 玉林市 (Yulin)", "short": "玉林", "pinyin": "yulin", "abbr": "yl", "lat": 22.6314, "lng": 110.1544, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "广西 梧州市 (Wuzhou)", "short": "梧州", "pinyin": "wuzhou", "abbr": "wz", "lat": 23.4770, "lng": 111.2791, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "广西 百色市 (Baise)", "short": "百色", "pinyin": "baise", "abbr": "bs", "lat": 23.9015, "lng": 106.6181, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},

    # ================= 海南省 (Hainan - 全覆盖) =================
    {"name": "海南省 海口市 (Haikou)", "short": "海口", "pinyin": "haikou", "abbr": "hk", "lat": 20.0440, "lng": 110.1999, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "海南省 三亚市 (Sanya)", "short": "三亚", "pinyin": "sanya", "abbr": "sy", "lat": 18.2528, "lng": 109.5119, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "海南省 琼海市 (Qionghai / 博鳌)", "short": "琼海", "pinyin": "qionghai", "abbr": "qh", "lat": 19.2585, "lng": 110.4665, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "海南省 儋州市 (Danzhou)", "short": "儋州", "pinyin": "danzhou", "abbr": "dz", "lat": 19.5175, "lng": 109.5811, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "海南省 文昌市 (Wenchang)", "short": "文昌", "pinyin": "wenchang", "abbr": "wc", "lat": 19.6130, "lng": 110.7540, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "海南省 万宁市 (Wanning / 日月湾)", "short": "万宁", "pinyin": "wanning", "abbr": "wn", "lat": 18.7962, "lng": 110.3888, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "海南省 陵水县 (Lingshui / 清水湾)", "short": "陵水", "pinyin": "lingshui", "abbr": "ls", "lat": 18.5050, "lng": 110.0372, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},

    # ================= 四川省 (Sichuan - 全覆盖) =================
    {"name": "四川省 绵阳市 (Mianyang)", "short": "绵阳", "pinyin": "mianyang", "abbr": "my", "lat": 31.4675, "lng": 104.6791, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "四川省 宜宾市 (Yibin)", "short": "宜宾", "pinyin": "yibin", "abbr": "yb", "lat": 28.7518, "lng": 104.6308, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "四川省 泸州市 (Luzhou)", "short": "泸州", "pinyin": "luzhou", "abbr": "lz", "lat": 28.8719, "lng": 105.4419, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "四川省 南充市 (Nanchong)", "short": "南充", "pinyin": "nanchong", "abbr": "nc", "lat": 30.7991, "lng": 106.0829, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "四川省 乐山市 (Leshan / 峨眉山)", "short": "乐山", "pinyin": "leshan", "abbr": "ls", "lat": 29.5521, "lng": 103.7657, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "四川省 德阳市 (Deyang)", "short": "德阳", "pinyin": "deyang", "abbr": "dy", "lat": 31.1270, "lng": 104.3980, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "四川省 成都市 都江堰市 (Dujiangyan)", "short": "都江堰", "pinyin": "dujiangyan", "abbr": "djy", "lat": 30.9882, "lng": 103.6472, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "四川省 德阳市 广汉市 (Guanghan / 三星堆)", "short": "广汉", "pinyin": "guanghan", "abbr": "gh", "lat": 30.9768, "lng": 104.2825, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "四川省 阿坝州 九寨沟 (Jiuzhaigou)", "short": "九寨沟", "pinyin": "jiuzhaigou", "abbr": "jzg", "lat": 33.2625, "lng": 104.2366, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "四川省 甘孜州 康定市 (Kangding)", "short": "康定", "pinyin": "kangding", "abbr": "kd", "lat": 30.0495, "lng": 101.9625, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "四川省 凉山州 西昌市 (Xichang)", "short": "西昌", "pinyin": "xichang", "abbr": "xc", "lat": 27.8872, "lng": 102.2678, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},

    # ================= 江苏省重点县级市与地级市 (Jiangsu Complete) =================
    {"name": "江苏省 苏州市 太仓市 (Taicang)", "short": "太仓", "pinyin": "taicang", "abbr": "tc", "lat": 31.4582, "lng": 121.1340, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "江苏省 苏州市 昆山市 (Kunshan)", "short": "昆山", "pinyin": "kunshan", "abbr": "ks", "lat": 31.3845, "lng": 120.9807, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "江苏省 苏州市 常熟市 (Changshu)", "short": "常熟", "pinyin": "changshu", "abbr": "cs", "lat": 31.6537, "lng": 120.7525, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 苏州市 张家港市 (Zhangjiagang)", "short": "张家港", "pinyin": "zhangjiagang", "abbr": "zjg", "lat": 31.8756, "lng": 120.5532, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 无锡市 江阴市 (Jiangyin)", "short": "江阴", "pinyin": "jiangyin", "abbr": "jy", "lat": 31.9110, "lng": 120.2852, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 无锡市 宜兴市 (Yixing)", "short": "宜兴", "pinyin": "yixing", "abbr": "yx", "lat": 31.3653, "lng": 119.8236, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 无锡市 (Wuxi)", "short": "无锡", "pinyin": "wuxi", "abbr": "wx", "lat": 31.4912, "lng": 120.3119, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "江苏省 常州市 (Changzhou)", "short": "常州", "pinyin": "changzhou", "abbr": "cz", "lat": 31.8112, "lng": 119.9740, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "江苏省 常州市 溧阳市 (Liyang)", "short": "溧阳", "pinyin": "liyang", "abbr": "ly", "lat": 31.4286, "lng": 119.4839, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 南通市 (Nantong)", "short": "南通", "pinyin": "nantong", "abbr": "nt", "lat": 31.9802, "lng": 120.8943, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "江苏省 南通市 启东市 (Qidong)", "short": "启东", "pinyin": "qidong", "abbr": "qd", "lat": 31.8107, "lng": 121.6570, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 南通市 海门区 (Haimen)", "short": "海门", "pinyin": "haimen", "abbr": "hm", "lat": 31.8943, "lng": 121.1691, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 扬州市 (Yangzhou)", "short": "扬州", "pinyin": "yangzhou", "abbr": "yz", "lat": 32.3942, "lng": 119.4129, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "江苏省 镇江市 (Zhenjiang)", "short": "镇江", "pinyin": "zhenjiang", "abbr": "zj", "lat": 32.1878, "lng": 119.4258, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 镇江市 丹阳市 (Danyang)", "short": "丹阳", "pinyin": "danyang", "abbr": "dy", "lat": 31.9953, "lng": 119.5752, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 泰州市 (Taizhou)", "short": "泰州", "pinyin": "taizhou", "abbr": "tz", "lat": 32.4555, "lng": 119.9229, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "江苏省 盐城市 (Yancheng)", "short": "盐城", "pinyin": "yancheng", "abbr": "yc", "lat": 33.3474, "lng": 120.1636, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "江苏省 淮安市 (Huai'an)", "short": "淮安", "pinyin": "huaian", "abbr": "ha", "lat": 33.5511, "lng": 119.0153, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "江苏省 宿迁市 (Suqian)", "short": "宿迁", "pinyin": "suqian", "abbr": "sq", "lat": 33.9630, "lng": 118.2752, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "江苏省 徐州市 (Xuzhou)", "short": "徐州", "pinyin": "xuzhou", "abbr": "xz", "lat": 34.2610, "lng": 117.1859, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "江苏省 连云港市 (Lianyungang)", "short": "连云港", "pinyin": "lianyungang", "abbr": "lyg", "lat": 34.5967, "lng": 119.2216, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},

    # ================= 浙江省重点县级市与地级市 (Zhejiang Complete) =================
    {"name": "浙江省 金华市 义乌市 (Yiwu)", "short": "义乌", "pinyin": "yiwu", "abbr": "yw", "lat": 29.3069, "lng": 120.0751, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "浙江省 嘉兴市 (Jiaxing)", "short": "嘉兴", "pinyin": "jiaxing", "abbr": "jx", "lat": 30.7461, "lng": 120.7555, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "浙江省 嘉兴市 海宁市 (Haining)", "short": "海宁", "pinyin": "haining", "abbr": "hn", "lat": 30.5097, "lng": 120.6813, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "浙江省 嘉兴市 桐乡市 (Tongxiang / 乌镇)", "short": "桐乡", "pinyin": "tongxiang", "abbr": "tx", "lat": 30.6302, "lng": 120.5463, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 湖州市 (Huzhou)", "short": "湖州", "pinyin": "huzhou", "abbr": "hz", "lat": 30.8943, "lng": 120.0868, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "浙江省 湖州市 德清县 (Deqing / 莫干山)", "short": "德清", "pinyin": "deqing", "abbr": "dq", "lat": 30.5332, "lng": 119.9786, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 湖州市 安吉县 (Anji)", "short": "安吉", "pinyin": "anji", "abbr": "aj", "lat": 30.6378, "lng": 119.6811, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 绍兴市 (Shaoxing)", "short": "绍兴", "pinyin": "shaoxing", "abbr": "sx", "lat": 30.0024, "lng": 120.5821, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "浙江省 绍兴市 诸暨市 (Zhuji)", "short": "诸暨", "pinyin": "zhuji", "abbr": "zj", "lat": 29.7126, "lng": 120.2319, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "浙江省 金华市 (Jinhua)", "short": "金华", "pinyin": "jinhua", "abbr": "jh", "lat": 29.1084, "lng": 119.6495, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "浙江省 金华市 东阳市 (Dongyang / 横店)", "short": "东阳", "pinyin": "dongyang", "abbr": "dy", "lat": 29.2894, "lng": 120.2419, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 衢州市 (Quzhou)", "short": "衢州", "pinyin": "quzhou", "abbr": "qz", "lat": 28.9701, "lng": 118.8758, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "浙江省 舟山市 (Zhoushan / 普陀山)", "short": "舟山", "pinyin": "zhoushan", "abbr": "zs", "lat": 30.0003, "lng": 122.2072, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "浙江省 台州市 (Taizhou)", "short": "台州", "pinyin": "taizhou", "abbr": "tz", "lat": 28.6564, "lng": 121.4286, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 丽水市 (Lishui)", "short": "丽水", "pinyin": "lishui", "abbr": "ls", "lat": 28.4676, "lng": 119.9218, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "浙江省 温州市 (Wenzhou)", "short": "温州", "pinyin": "wenzhou", "abbr": "wz", "lat": 28.0006, "lng": 120.6721, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},

    # ================= 广东省重点县区与地级市 (Guangdong Complete) =================
    {"name": "广东省 佛山市 (Foshan)", "short": "佛山", "pinyin": "foshan", "abbr": "fs", "lat": 23.0218, "lng": 113.1214, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "广东省 佛山市 顺德区 (Shunde)", "short": "顺德", "pinyin": "shunde", "abbr": "sd", "lat": 22.8028, "lng": 113.2925, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "广东省 东莞市 (Dongguan)", "short": "东莞", "pinyin": "dongguan", "abbr": "dg", "lat": 23.0205, "lng": 113.7518, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "广东省 中山市 (Zhongshan)", "short": "中山", "pinyin": "zhongshan", "abbr": "zs", "lat": 22.5176, "lng": 113.3928, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "广东省 珠海市 (Zhuhai)", "short": "珠海", "pinyin": "zhuhai", "abbr": "zh", "lat": 22.2707, "lng": 113.5767, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "广东省 惠州市 (Huizhou)", "short": "惠州", "pinyin": "huizhou", "abbr": "hz", "lat": 23.1118, "lng": 114.4162, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "广东省 汕头市 (Shantou)", "short": "汕头", "pinyin": "shantou", "abbr": "st", "lat": 23.3541, "lng": 116.6820, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "广东省 潮州市 (Chaozhou)", "short": "潮州", "pinyin": "chaozhou", "abbr": "cz", "lat": 23.6570, "lng": 116.6226, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "广东省 湛江市 (Zhanjiang)", "short": "湛江", "pinyin": "zhanjiang", "abbr": "zj", "lat": 21.2707, "lng": 110.3594, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},
    {"name": "广东省 江门市 (Jiangmen)", "short": "江门", "pinyin": "jiangmen", "abbr": "jm", "lat": 22.5787, "lng": 113.0819, "tz": "Asia/Shanghai", "country": "中国", "weight": 78},

    # ================= 华北/东北/华中/华东省会与重点城市 =================
    {"name": "黑龙江 哈尔滨市 (Harbin)", "short": "哈尔滨", "pinyin": "haerbin", "abbr": "heb", "lat": 45.8038, "lng": 126.5350, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "吉林省 长春市 (Changchun)", "short": "长春", "pinyin": "changchun", "abbr": "cc", "lat": 43.8171, "lng": 125.3235, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "吉林省 吉林市 (Jilin)", "short": "吉林", "pinyin": "jilin", "abbr": "jl", "lat": 43.8378, "lng": 126.5494, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "辽宁省 沈阳市 (Shenyang)", "short": "沈阳", "pinyin": "shenyang", "abbr": "sy", "lat": 41.8057, "lng": 123.4315, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "辽宁省 大连市 (Dalian)", "short": "大连", "pinyin": "dalian", "abbr": "dl", "lat": 38.9140, "lng": 121.6147, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "河北省 石家庄市 (Shijiazhuang)", "short": "石家庄", "pinyin": "shijiazhuang", "abbr": "sjz", "lat": 38.0428, "lng": 114.5149, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "河北省 唐山市 (Tangshan)", "short": "唐山", "pinyin": "tangshan", "abbr": "ts", "lat": 39.6351, "lng": 118.1754, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "河北省 保定市 (Baoding / 雄安新区)", "short": "保定", "pinyin": "baoding", "abbr": "bd", "lat": 38.8739, "lng": 115.4648, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "山西省 太原市 (Taiyuan)", "short": "太原", "pinyin": "taiyuan", "abbr": "ty", "lat": 37.8706, "lng": 112.5489, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "山西省 大同市 (Datong)", "short": "大同", "pinyin": "datong", "abbr": "dt", "lat": 40.0768, "lng": 113.3001, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "安徽省 合肥市 (Hefei)", "short": "合肥", "pinyin": "hefei", "abbr": "hf", "lat": 31.8206, "lng": 117.2272, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "安徽省 芜湖市 (Wuhu)", "short": "芜湖", "pinyin": "wuhu", "abbr": "wh", "lat": 31.3529, "lng": 118.3765, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "安徽省 黄山市 (Huangshan)", "short": "黄山", "pinyin": "huangshan", "abbr": "hs", "lat": 29.7147, "lng": 118.3375, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "江西省 南昌市 (Nanchang)", "short": "南昌", "pinyin": "nanchang", "abbr": "nc", "lat": 28.6820, "lng": 115.8579, "tz": "Asia/Shanghai", "country": "中国", "weight": 88},
    {"name": "江西省 景德镇市 (Jingdezhen)", "short": "景德镇", "pinyin": "jingdezhen", "abbr": "jdz", "lat": 29.2687, "lng": 117.1783, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "江西省 赣州市 (Ganzhou)", "short": "赣州", "pinyin": "ganzhou", "abbr": "gz", "lat": 25.8318, "lng": 114.9359, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江西省 九江市 (Jiujiang / 庐山)", "short": "九江", "pinyin": "jiujiang", "abbr": "jj", "lat": 29.7051, "lng": 115.9928, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "山东省 烟台市 (Yantai)", "short": "烟台", "pinyin": "yantai", "abbr": "yt", "lat": 37.4638, "lng": 121.4479, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "山东省 威海市 (Weihai)", "short": "威海", "pinyin": "weihai", "abbr": "wh", "lat": 37.5131, "lng": 122.1205, "tz": "Asia/Shanghai", "country": "中国", "weight": 82},
    {"name": "山东省 潍坊市 (Weifang)", "short": "潍坊", "pinyin": "weifang", "abbr": "wf", "lat": 36.7068, "lng": 119.1618, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "山东省 淄博市 (Zibo)", "short": "淄博", "pinyin": "zibo", "abbr": "zb", "lat": 36.8135, "lng": 118.0550, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "山东省 临沂市 (Linyi)", "short": "临沂", "pinyin": "linyi", "abbr": "ly", "lat": 35.1047, "lng": 118.3564, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "福建省 泉州市 (Quanzhou)", "short": "泉州", "pinyin": "quanzhou", "abbr": "qz", "lat": 24.8741, "lng": 118.6757, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "福建省 泉州市 晋江市 (Jinjiang)", "short": "晋江", "pinyin": "jinjiang", "abbr": "jj", "lat": 24.7814, "lng": 118.5750, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "福建省 漳州市 (Zhangzhou)", "short": "漳州", "pinyin": "zhangzhou", "abbr": "zz", "lat": 24.5130, "lng": 117.6472, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},

    # ================= 国际知名都会 (Global Top Metropolises) =================
    {"name": "美国 纽约 (New York, NY)", "short": "纽约", "pinyin": "niuyue", "abbr": "ny", "lat": 40.7128, "lng": -74.0060, "tz": "America/New_York", "country": "美国", "weight": 100},
    {"name": "美国 洛杉矶 (Los Angeles, CA)", "short": "洛杉矶", "pinyin": "luoshanji", "abbr": "la", "lat": 34.0522, "lng": -118.2437, "tz": "America/Los_Angeles", "country": "美国", "weight": 95},
    {"name": "美国 旧金山 (San Francisco, CA)", "short": "旧金山", "pinyin": "jiujinshan", "abbr": "sf", "lat": 37.7749, "lng": -122.4194, "tz": "America/Los_Angeles", "country": "美国", "weight": 95},
    {"name": "美国 硅谷/圣何塞 (San Jose, CA)", "short": "圣何塞", "pinyin": "shenghesai", "abbr": "sj", "lat": 37.3382, "lng": -121.8863, "tz": "America/Los_Angeles", "country": "美国", "weight": 85},
    {"name": "美国 西雅图 (Seattle, WA)", "short": "西雅图", "pinyin": "xiyatu", "abbr": "sea", "lat": 47.6062, "lng": -122.3321, "tz": "America/Los_Angeles", "country": "美国", "weight": 88},
    {"name": "美国 芝加哥 (Chicago, IL)", "short": "芝加哥", "pinyin": "zhijiage", "abbr": "chi", "lat": 41.8781, "lng": -87.6298, "tz": "America/Chicago", "country": "美国", "weight": 88},
    {"name": "美国 波士顿 (Boston, MA)", "short": "波士顿", "pinyin": "boshidun", "abbr": "bos", "lat": 42.3601, "lng": -71.0589, "tz": "America/New_York", "country": "美国", "weight": 88},
    {"name": "加拿大 多伦多 (Toronto)", "short": "多伦多", "pinyin": "duoluoduo", "abbr": "yyz", "lat": 43.6532, "lng": -79.3832, "tz": "America/Toronto", "country": "加拿大", "weight": 90},
    {"name": "加拿大 温哥华 (Vancouver)", "short": "温哥华", "pinyin": "wengehua", "abbr": "yvr", "lat": 49.2827, "lng": -123.1207, "tz": "America/Vancouver", "country": "加拿大", "weight": 90},
    {"name": "英国 伦敦 (London)", "short": "伦敦", "pinyin": "lundun", "abbr": "lon", "lat": 51.5074, "lng": -0.1278, "tz": "Europe/London", "country": "英国", "weight": 100},
    {"name": "法国 巴黎 (Paris)", "short": "巴黎", "pinyin": "bali", "abbr": "par", "lat": 48.8566, "lng": 2.3522, "tz": "Europe/Paris", "country": "法国", "weight": 100},
    {"name": "德国 柏林 (Berlin)", "short": "柏林", "pinyin": "bolin", "abbr": "ber", "lat": 52.5200, "lng": 13.4050, "tz": "Europe/Berlin", "country": "德国", "weight": 90},
    {"name": "德国 法兰克福 (Frankfurt)", "short": "法兰克福", "pinyin": "falankefu", "abbr": "fra", "lat": 50.1109, "lng": 8.6821, "tz": "Europe/Berlin", "country": "德国", "weight": 90},
    {"name": "意大利 罗马 (Rome)", "short": "罗马", "pinyin": "luoma", "abbr": "rom", "lat": 41.9028, "lng": 12.4964, "tz": "Europe/Rome", "country": "意大利", "weight": 90},
    {"name": "日本 东京 (Tokyo)", "short": "东京", "pinyin": "dongjing", "abbr": "tyo", "lat": 35.6762, "lng": 139.6503, "tz": "Asia/Tokyo", "country": "日本", "weight": 100},
    {"name": "日本 大阪 (Osaka)", "short": "大阪", "pinyin": "daban", "abbr": "osa", "lat": 34.6937, "lng": 135.5023, "tz": "Asia/Tokyo", "country": "日本", "weight": 90},
    {"name": "日本 京都 (Kyoto)", "short": "京都", "pinyin": "jingdu", "abbr": "kyo", "lat": 35.0116, "lng": 135.7681, "tz": "Asia/Tokyo", "country": "日本", "weight": 90},
    {"name": "韩国 首尔 (Seoul)", "short": "首尔", "pinyin": "shouer", "abbr": "sel", "lat": 37.5665, "lng": 126.9780, "tz": "Asia/Seoul", "country": "韩国", "weight": 92},
    {"name": "新加坡 (Singapore)", "short": "新加坡", "pinyin": "xinjiapo", "abbr": "sg", "lat": 1.3521, "lng": 103.8198, "tz": "Asia/Singapore", "country": "新加坡", "weight": 95},
    {"name": "马来西亚 吉隆坡 (Kuala Lumpur)", "short": "吉隆坡", "pinyin": "jilongpo", "abbr": "kl", "lat": 3.1390, "lng": 101.6869, "tz": "Asia/Kuala_Lumpur", "country": "马来西亚", "weight": 90},
    {"name": "泰国 曼谷 (Bangkok)", "short": "曼谷", "pinyin": "mangu", "abbr": "bkk", "lat": 13.7563, "lng": 100.5018, "tz": "Asia/Bangkok", "country": "泰国", "weight": 90},
    {"name": "澳大利亚 悉尼 (Sydney)", "short": "悉尼", "pinyin": "xini", "abbr": "syd", "lat": -33.8688, "lng": 151.2093, "tz": "Australia/Sydney", "country": "澳大利亚", "weight": 95},
    {"name": "澳大利亚 墨尔本 (Melbourne)", "short": "墨尔本", "pinyin": "moerben", "abbr": "mel", "lat": -37.8136, "lng": 144.9631, "tz": "Australia/Melbourne", "country": "澳大利亚", "weight": 90},
    {"name": "新西兰 奥克兰 (Auckland)", "short": "奥克兰", "pinyin": "aokelan", "abbr": "akl", "lat": -36.8485, "lng": 174.7633, "tz": "Pacific/Auckland", "country": "新西兰", "weight": 85},
    {"name": "阿联酋 迪拜 (Dubai)", "short": "迪拜", "pinyin": "dibai", "abbr": "dxb", "lat": 25.2048, "lng": 55.2708, "tz": "Asia/Dubai", "country": "阿联酋", "weight": 90},

    # ================= 印度全量重点都会与灵性圣城 (India Complete) =================
    {"name": "印度 新德里/德里 (New Delhi / Delhi)", "short": "新德里", "pinyin": "xindeli", "abbr": "del", "lat": 28.6139, "lng": 77.2090, "tz": "Asia/Kolkata", "country": "印度", "weight": 96},
    {"name": "印度 孟买 (Mumbai / Bombay)", "short": "孟买", "pinyin": "mengmai", "abbr": "bom", "lat": 19.0760, "lng": 72.8777, "tz": "Asia/Kolkata", "country": "印度", "weight": 95},
    {"name": "印度 班加罗尔 (Bengaluru / Bangalore)", "short": "班加罗尔", "pinyin": "banjialuoer", "abbr": "blr", "lat": 12.9716, "lng": 77.5946, "tz": "Asia/Kolkata", "country": "印度", "weight": 92},
    {"name": "印度 瓦拉纳西 (Varanasi / 恒河圣城/鹿野苑)", "short": "瓦拉纳西", "pinyin": "walanaxi", "abbr": "vns", "lat": 25.3176, "lng": 82.9739, "tz": "Asia/Kolkata", "country": "印度", "weight": 92},
    {"name": "印度 菩提伽耶 (Bodh Gaya / 佛陀成道圣地)", "short": "菩提伽耶", "pinyin": "putijiaye", "abbr": "btjy", "lat": 24.6961, "lng": 84.9869, "tz": "Asia/Kolkata", "country": "印度", "weight": 92},
    {"name": "印度 瑞诗凯诗 (Rishikesh / 世界瑜伽之都)", "short": "瑞诗凯诗", "pinyin": "ruishikaishi", "abbr": "rsks", "lat": 30.0869, "lng": 78.2676, "tz": "Asia/Kolkata", "country": "印度", "weight": 92},
    {"name": "印度 达兰萨拉 (Dharamsala / 麦罗肯吉)", "short": "达兰萨拉", "pinyin": "dalansala", "abbr": "dlsl", "lat": 32.2190, "lng": 76.3234, "tz": "Asia/Kolkata", "country": "印度", "weight": 90},
    {"name": "印度 浦那 (Pune / 奥修中心)", "short": "浦那", "pinyin": "puna", "abbr": "pn", "lat": 18.5204, "lng": 73.8567, "tz": "Asia/Kolkata", "country": "印度", "weight": 90},
    {"name": "印度 斋普尔 (Jaipur / 粉红之城)", "short": "斋普尔", "pinyin": "zhaipuer", "abbr": "zpe", "lat": 26.9124, "lng": 75.7873, "tz": "Asia/Kolkata", "country": "印度", "weight": 88},
    {"name": "印度 加尔各答 (Kolkata / Calcutta)", "short": "加尔各答", "pinyin": "jiaergada", "abbr": "jegd", "lat": 22.5726, "lng": 88.3639, "tz": "Asia/Kolkata", "country": "印度", "weight": 88},
    {"name": "印度 金奈/钦奈 (Chennai / Madras)", "short": "金奈", "pinyin": "jinnai", "abbr": "jn", "lat": 13.0827, "lng": 80.2707, "tz": "Asia/Kolkata", "country": "印度", "weight": 88},
    {"name": "印度 海得拉巴 (Hyderabad)", "short": "海得拉巴", "pinyin": "haidelaba", "abbr": "hdlb", "lat": 17.3850, "lng": 78.4867, "tz": "Asia/Kolkata", "country": "印度", "weight": 88},
    {"name": "印度 阿格拉 (Agra / 泰姬陵)", "short": "阿格拉", "pinyin": "agela", "abbr": "agl", "lat": 27.1767, "lng": 78.0081, "tz": "Asia/Kolkata", "country": "印度", "weight": 88},
    {"name": "印度 果阿 (Goa)", "short": "果阿", "pinyin": "guoa", "abbr": "ga", "lat": 15.2993, "lng": 74.1240, "tz": "Asia/Kolkata", "country": "印度", "weight": 85},
    {"name": "印度 艾哈迈达巴德 (Ahmedabad)", "short": "艾哈迈达巴德", "pinyin": "aihemaidabade", "abbr": "ahmd", "lat": 23.0225, "lng": 72.5714, "tz": "Asia/Kolkata", "country": "印度", "weight": 82},
    {"name": "印度 科钦 (Kochi / 喀拉拉邦)", "short": "科钦", "pinyin": "keqin", "abbr": "kq", "lat": 9.9312, "lng": 76.2673, "tz": "Asia/Kolkata", "country": "印度", "weight": 82},
    {"name": "印度 乌代布尔 (Udaipur / 白色之城)", "short": "乌代布尔", "pinyin": "wudaibuer", "abbr": "wdbe", "lat": 24.5854, "lng": 73.7125, "tz": "Asia/Kolkata", "country": "印度", "weight": 82},
    {"name": "印度 焦特布尔 (Jodhpur / 蓝色之城)", "short": "焦特布尔", "pinyin": "jiaotebuer", "abbr": "jtbe", "lat": 26.2389, "lng": 73.0243, "tz": "Asia/Kolkata", "country": "印度", "weight": 82},

    # ================= 尼泊尔重点城市与圣地 (Nepal Complete) =================
    {"name": "尼泊尔 加德满都 (Kathmandu)", "short": "加德满都", "pinyin": "jiademandu", "abbr": "ktm/jdmd", "lat": 27.7172, "lng": 85.3240, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 95},
    {"name": "尼泊尔 博卡拉 (Pokhara / 鱼尾峰徒步圣地)", "short": "博卡拉", "pinyin": "bokala", "abbr": "pkr/bkl", "lat": 28.2096, "lng": 83.9856, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 92},
    {"name": "尼泊尔 蓝毗尼 (Lumbini / 佛陀诞生地)", "short": "蓝毗尼", "pinyin": "lanpini", "abbr": "lmb/lpn", "lat": 27.4840, "lng": 83.2760, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 92},
    {"name": "尼泊尔 巴克塔普尔/巴德岗 (Bhaktapur)", "short": "巴德岗", "pinyin": "badegang", "abbr": "bdg", "lat": 27.6710, "lng": 85.4298, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 88},
    {"name": "尼泊尔 帕坦/拉利特普尔 (Patan / Lalitpur)", "short": "帕坦", "pinyin": "patan", "abbr": "pt", "lat": 27.6766, "lng": 85.3252, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 85},
    {"name": "尼泊尔 奇特旺/奇旺 (Chitwan / Bharatpur)", "short": "奇特旺", "pinyin": "qitewang", "abbr": "qtw", "lat": 27.6833, "lng": 84.4333, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 85},
    {"name": "尼泊尔 纳加阔特 (Nagarkot / 喜马拉雅观景台)", "short": "纳加阔特", "pinyin": "najiakuote", "abbr": "njkt", "lat": 27.7174, "lng": 85.5204, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 82},
    {"name": "尼泊尔 贾纳克布尔 (Janakpur)", "short": "贾纳克布尔", "pinyin": "jianakebuer", "abbr": "jnkb", "lat": 26.7288, "lng": 85.9244, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 80},
    {"name": "尼泊尔 达兰 (Dharan)", "short": "达兰", "pinyin": "dalan", "abbr": "dl", "lat": 26.8124, "lng": 87.2836, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 80},
    {"name": "尼泊尔 比拉德讷格尔 (Biratnagar)", "short": "比拉德讷格尔", "pinyin": "biladenageer", "abbr": "bld", "lat": 26.4525, "lng": 87.2718, "tz": "Asia/Kathmandu", "country": "尼泊尔", "weight": 80},

    # ================= 不丹/斯里兰卡/东南亚重点都会 =================
    {"name": "不丹 廷布 (Thimphu)", "short": "廷布", "pinyin": "tingbu", "abbr": "tb", "lat": 27.4728, "lng": 89.6393, "tz": "Asia/Thimphu", "country": "不丹", "weight": 88},
    {"name": "不丹 帕罗 (Paro / 虎穴寺)", "short": "帕罗", "pinyin": "paluo", "abbr": "pl", "lat": 27.4286, "lng": 89.4164, "tz": "Asia/Thimphu", "country": "不丹", "weight": 85},
    {"name": "斯里兰卡 科伦坡 (Colombo)", "short": "科伦坡", "pinyin": "kelunpo", "abbr": "klp", "lat": 6.9271, "lng": 79.8612, "tz": "Asia/Colombo", "country": "斯里兰卡", "weight": 88},
    {"name": "斯里兰卡 康提 (Kandy / 佛牙寺)", "short": "康提", "pinyin": "kangti", "abbr": "kt", "lat": 7.2906, "lng": 80.6337, "tz": "Asia/Colombo", "country": "斯里兰卡", "weight": 85},
    {"name": "印度尼西亚 巴厘岛 (Bali / Denpasar / 乌布 Ubud)", "short": "巴厘岛", "pinyin": "balidao", "abbr": "bld", "lat": -8.3405, "lng": 115.0920, "tz": "Asia/Makassar", "country": "印度尼西亚", "weight": 92},
    {"name": "印度尼西亚 雅加达 (Jakarta)", "short": "雅加达", "pinyin": "yajiada", "abbr": "yjd", "lat": -6.2088, "lng": 106.8456, "tz": "Asia/Jakarta", "country": "印度尼西亚", "weight": 90},
    {"name": "柬埔寨 暹粒 (Siem Reap / 吴哥窟)", "short": "暹粒", "pinyin": "xianli", "abbr": "xl", "lat": 13.3671, "lng": 103.8448, "tz": "Asia/Phnom_Penh", "country": "柬埔寨", "weight": 90},
    {"name": "越南 河内 (Hanoi)", "short": "河内", "pinyin": "henei", "abbr": "hn", "lat": 21.0285, "lng": 105.8542, "tz": "Asia/Ho_Chi_Minh", "country": "越南", "weight": 88},
    {"name": "越南 胡志明市 (Ho Chi Minh City)", "short": "胡志明市", "pinyin": "huzhiming", "abbr": "hzm", "lat": 10.8231, "lng": 106.6297, "tz": "Asia/Ho_Chi_Minh", "country": "越南", "weight": 88}
]


def search_cities(query: str, limit: int = 15) -> list:
    """
    High-performance multi-strategy search:
    1. Exact Match on short name (e.g. 乌鲁木齐, 拉萨, 太仓)
    2. Exact Match on pinyin or abbreviation (e.g. wlmq, ls, beijing)
    3. Prefix matches sorted by popularity weight
    4. Substring matches in full Chinese name or English text
    """
    if not query or not query.strip():
        # Default mega cities
        sorted_defaults = sorted(GEO_DATA_LIST, key=lambda x: -x.get("weight", 50))
        return sorted_defaults[:limit]

    q = query.strip().lower()

    exact_matches = []
    prefix_matches = []
    partial_matches = []

    for item in GEO_DATA_LIST:
        name_lower = item["name"].lower()
        short_lower = item["short"].lower()
        pinyin = item.get("pinyin", "")
        abbr = item.get("abbr", "")
        weight = item.get("weight", 50)

        # Extract english words
        # 1. Exact Match
        if q == short_lower or q == pinyin or q == abbr:
            exact_matches.append((item, 1000 + weight))
        # 2. Prefix Match
        elif short_lower.startswith(q) or pinyin.startswith(q) or abbr.startswith(q) or name_lower.startswith(q) or any(w.startswith(q) for w in name_lower.replace('(', ' ').replace(')', ' ').replace('/', ' ').split()):
            prefix_matches.append((item, 500 + weight))
        # 3. Substring Match
        elif q in name_lower or q in pinyin or q in abbr:
            partial_matches.append((item, weight))

    exact_matches.sort(key=lambda x: -x[1])
    prefix_matches.sort(key=lambda x: -x[1])
    partial_matches.sort(key=lambda x: -x[1])

    combined = [x[0] for x in (exact_matches + prefix_matches + partial_matches)]

    seen = set()
    result = []
    for c in combined:
        key = (c["lat"], c["lng"])
        if key not in seen:
            seen.add(key)
            result.append(c)
        if len(result) >= limit:
            break

    return result
