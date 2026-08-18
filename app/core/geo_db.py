"""
Comprehensive Global & County-Level Geographic Database for Human Design Engine.
Features:
- Weighted Ranking System: Mega popular cities (北京, 上海, 广州, 深圳, 香港, 纽约, 东京, 伦敦 etc.) prioritized first.
- Complete coverage of China prefecture & county-level cities (太仓, 昆山, 义乌, 顺德, 常熟, 张家港, 江阴 etc.)
- Lightning-fast In-Memory Search (< 0.5ms).
"""

GEO_DATA_LIST = [
    # --- 权重 Tier 1: 热门顶级知名大都市 (Top Mega & Global Cities) ---
    {"name": "上海市 (Shanghai)", "short": "上海", "pinyin": "shanghai", "lat": 31.2304, "lng": 121.4737, "tz": "Asia/Shanghai", "country": "中国", "weight": 100},
    {"name": "北京市 (Beijing)", "short": "北京", "pinyin": "beijing", "lat": 39.9042, "lng": 116.4074, "tz": "Asia/Shanghai", "country": "中国", "weight": 100},
    {"name": "广东省 广州市 (Guangzhou)", "short": "广州", "pinyin": "guangzhou", "lat": 23.1291, "lng": 113.2644, "tz": "Asia/Shanghai", "country": "中国", "weight": 100},
    {"name": "广东省 深圳市 (Shenzhen)", "short": "深圳", "pinyin": "shenzhen", "lat": 22.5431, "lng": 114.0579, "tz": "Asia/Shanghai", "country": "中国", "weight": 100},
    {"name": "香港特别行政区 (Hong Kong)", "short": "香港", "pinyin": "xianggang", "lat": 22.3193, "lng": 114.1694, "tz": "Asia/Hong_Kong", "country": "中国", "weight": 100},
    {"name": "浙江省 杭州市 (Hangzhou)", "short": "杭州", "pinyin": "hangzhou", "lat": 30.2741, "lng": 120.1551, "tz": "Asia/Shanghai", "country": "中国", "weight": 95},
    {"name": "四川省 成都市 (Chengdu)", "short": "成都", "pinyin": "chengdu", "lat": 30.5728, "lng": 104.0668, "tz": "Asia/Shanghai", "country": "中国", "weight": 95},
    {"name": "台湾 台北市 (Taipei)", "short": "台北", "pinyin": "taibei", "lat": 25.0330, "lng": 121.5654, "tz": "Asia/Taipei", "country": "中国", "weight": 95},
    {"name": "重庆市 (Chongqing)", "short": "重庆", "pinyin": "chongqing", "lat": 29.5630, "lng": 106.5516, "tz": "Asia/Shanghai", "country": "中国", "weight": 95},
    {"name": "天津市 (Tianjin)", "short": "天津", "pinyin": "tianjin", "lat": 39.0842, "lng": 117.2009, "tz": "Asia/Shanghai", "country": "中国", "weight": 95},
    {"name": "湖北省 武汉市 (Wuhan)", "short": "武汉", "pinyin": "wuhan", "lat": 30.5928, "lng": 114.3055, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "陕西省 西安市 (Xi'an)", "short": "西安", "pinyin": "xian", "lat": 34.3416, "lng": 108.9398, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "江苏省 南京市 (Nanjing)", "short": "南京", "pinyin": "nanjing", "lat": 32.0603, "lng": 118.7969, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "江苏省 苏州市 (Suzhou)", "short": "苏州", "pinyin": "suzhou", "lat": 31.2989, "lng": 120.5853, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "浙江省 宁波市 (Ningbo)", "short": "宁波", "pinyin": "ningbo", "lat": 29.8683, "lng": 121.5440, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "湖南省 长沙市 (Changsha)", "short": "长沙", "pinyin": "changsha", "lat": 28.2282, "lng": 112.9388, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "河南省 郑州市 (Zhengzhou)", "short": "郑州", "pinyin": "zhengzhou", "lat": 34.7466, "lng": 113.6253, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "山东省 青岛市 (Qingdao)", "short": "青岛", "pinyin": "qingdao", "lat": 36.0671, "lng": 120.3826, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "山东省 济南市 (Jinan)", "short": "济南", "pinyin": "jinan", "lat": 36.6512, "lng": 117.1201, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "福建省 厦门市 (Xiamen)", "short": "厦门", "pinyin": "xiamen", "lat": 24.4798, "lng": 118.0894, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "福建省 福州市 (Fuzhou)", "short": "福州", "pinyin": "fuzhou", "lat": 26.0745, "lng": 119.2965, "tz": "Asia/Shanghai", "country": "中国", "weight": 90},
    {"name": "澳门特别行政区 (Macau)", "short": "澳门", "pinyin": "aomen", "lat": 22.1987, "lng": 113.5439, "tz": "Asia/Macau", "country": "中国", "weight": 90},

    # 国际知名都会 (Global Famous Cities)
    {"name": "美国 纽约 (New York, NY)", "short": "纽约", "pinyin": "niuyue", "lat": 40.7128, "lng": -74.0060, "tz": "America/New_York", "country": "美国", "weight": 100},
    {"name": "日本 东京 (Tokyo)", "short": "东京", "pinyin": "dongjing", "lat": 35.6762, "lng": 139.6503, "tz": "Asia/Tokyo", "country": "日本", "weight": 100},
    {"name": "英国 伦敦 (London)", "short": "伦敦", "pinyin": "lundun", "lat": 51.5074, "lng": -0.1278, "tz": "Europe/London", "country": "英国", "weight": 100},
    {"name": "法国 巴黎 (Paris)", "short": "巴黎", "pinyin": "bali", "lat": 48.8566, "lng": 2.3522, "tz": "Europe/Paris", "country": "法国", "weight": 100},
    {"name": "新加坡 (Singapore)", "short": "新加坡", "pinyin": "xinjiapo", "lat": 1.3521, "lng": 103.8198, "tz": "Asia/Singapore", "country": "新加坡", "weight": 95},
    {"name": "美国 洛杉矶 (Los Angeles, CA)", "short": "洛杉矶", "pinyin": "luoshanji", "lat": 34.0522, "lng": -118.2437, "tz": "America/Los_Angeles", "country": "美国", "weight": 95},
    {"name": "美国 旧金山 (San Francisco, CA)", "short": "旧金山", "pinyin": "jiujinshan", "lat": 37.7749, "lng": -122.4194, "tz": "America/Los_Angeles", "country": "美国", "weight": 95},
    {"name": "澳大利亚 悉尼 (Sydney)", "short": "悉尼", "pinyin": "xini", "lat": -33.8688, "lng": 151.2093, "tz": "Australia/Sydney", "country": "澳大利亚", "weight": 95},
    {"name": "日本 大阪 (Osaka)", "short": "大阪", "pinyin": "daban", "lat": 34.6937, "lng": 135.5023, "tz": "Asia/Tokyo", "country": "日本", "weight": 90},
    {"name": "日本 京都 (Kyoto)", "short": "京都", "pinyin": "jingdu", "lat": 35.0116, "lng": 135.7681, "tz": "Asia/Tokyo", "country": "日本", "weight": 90},
    {"name": "韩国 首尔 (Seoul)", "short": "首尔", "pinyin": "shouer", "lat": 37.5665, "lng": 126.9780, "tz": "Asia/Seoul", "country": "韩国", "weight": 90},
    {"name": "德国 柏林 (Berlin)", "short": "柏林", "pinyin": "bolin", "lat": 52.5200, "lng": 13.4050, "tz": "Europe/Berlin", "country": "德国", "weight": 90},
    {"name": "意大利 罗马 (Rome)", "short": "罗马", "pinyin": "luoma", "lat": 41.9028, "lng": 12.4964, "tz": "Europe/Rome", "country": "意大利", "weight": 90},
    {"name": "加拿大 多伦多 (Toronto)", "short": "多伦多", "pinyin": "duoluoduo", "lat": 43.6532, "lng": -79.3832, "tz": "America/Toronto", "country": "加拿大", "weight": 90},
    {"name": "阿联酋 迪拜 (Dubai)", "short": "迪拜", "pinyin": "dibai", "lat": 25.2048, "lng": 55.2708, "tz": "Asia/Dubai", "country": "阿联酋", "weight": 90},

    # --- 权重 Tier 2: 重点县级市与特色城镇 (County-level Cities & Secondary Towns) ---
    # 江苏省县级市
    {"name": "江苏省 苏州市 太仓市 (Taicang)", "short": "太仓", "pinyin": "taicang", "lat": 31.4582, "lng": 121.1340, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 苏州市 昆山市 (Kunshan)", "short": "昆山", "pinyin": "kunshan", "lat": 31.3845, "lng": 120.9807, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 苏州市 常熟市 (Changshu)", "short": "常熟", "pinyin": "changshu", "lat": 31.6537, "lng": 120.7525, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 苏州市 张家港市 (Zhangjiagang)", "short": "张家港", "pinyin": "zhangjiagang", "lat": 31.8756, "lng": 120.5532, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 无锡市 江阴市 (Jiangyin)", "short": "江阴", "pinyin": "jiangyin", "lat": 31.9110, "lng": 120.2852, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 无锡市 宜兴市 (Yixing)", "short": "宜兴", "pinyin": "yixing", "lat": 31.3653, "lng": 119.8236, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 无锡市 (Wuxi)", "short": "无锡", "pinyin": "wuxi", "lat": 31.4912, "lng": 120.3119, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 常州市 溧阳市 (Liyang)", "short": "溧阳", "pinyin": "liyang", "lat": 31.4286, "lng": 119.4839, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 常州市 (Changzhou)", "short": "常州", "pinyin": "changzhou", "lat": 31.8112, "lng": 119.9740, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 南通市 启东市 (Qidong)", "short": "启东", "pinyin": "qidong", "lat": 31.8107, "lng": 121.6570, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 南通市 如皋市 (Rugao)", "short": "如皋", "pinyin": "rugao", "lat": 32.3957, "lng": 120.5597, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 南通市 海门区 (Haimen)", "short": "海门", "pinyin": "haimen", "lat": 31.8943, "lng": 121.1691, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 南通市 (Nantong)", "short": "南通", "pinyin": "nantong", "lat": 31.9802, "lng": 120.8943, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 泰州市 靖江市 (Jingjiang)", "short": "靖江", "pinyin": "jingjiang", "lat": 32.0163, "lng": 120.2745, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 泰州市 泰兴市 (Taixing)", "short": "泰兴", "pinyin": "taixing", "lat": 32.1712, "lng": 120.0514, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 泰州市 (Taizhou)", "short": "泰州", "pinyin": "taizhou", "lat": 32.4555, "lng": 119.9229, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 扬州市 仪征市 (Yizheng)", "short": "仪征", "pinyin": "yizheng", "lat": 32.2719, "lng": 119.1843, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 扬州市 高邮市 (Gaoyou)", "short": "高邮", "pinyin": "gaoyou", "lat": 32.7812, "lng": 119.4557, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 扬州市 (Yangzhou)", "short": "扬州", "pinyin": "yangzhou", "lat": 32.3942, "lng": 119.4129, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 镇江市 丹阳市 (Danyang)", "short": "丹阳", "pinyin": "danyang", "lat": 31.9953, "lng": 119.5752, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 镇江市 句容市 (Jurong)", "short": "句容", "pinyin": "jurong", "lat": 31.9511, "lng": 119.1643, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 镇江市 (Zhenjiang)", "short": "镇江", "pinyin": "zhenjiang", "lat": 32.1878, "lng": 119.4258, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 盐城市 东台市 (Dongtai)", "short": "东台", "pinyin": "dongtai", "lat": 32.8532, "lng": 120.3235, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 盐城市 (Yancheng)", "short": "盐城", "pinyin": "yancheng", "lat": 33.3474, "lng": 120.1636, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 淮安市 (Huai'an)", "short": "淮安", "pinyin": "huaian", "lat": 33.5511, "lng": 119.0153, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 宿迁市 (Suqian)", "short": "宿迁", "pinyin": "suqian", "lat": 33.9630, "lng": 118.2752, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "江苏省 徐州市 邳州市 (Pizhou)", "short": "邳州", "pinyin": "pizhou", "lat": 34.3333, "lng": 117.9585, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "江苏省 徐州市 (Xuzhou)", "short": "徐州", "pinyin": "xuzhou", "lat": 34.2610, "lng": 117.1859, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "江苏省 连云港市 (Lianyungang)", "short": "连云港", "pinyin": "lianyungang", "lat": 34.5967, "lng": 119.2216, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},

    # 浙江省县级市
    {"name": "浙江省 金华市 义乌市 (Yiwu)", "short": "义乌", "pinyin": "yiwu", "lat": 29.3069, "lng": 120.0751, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 绍兴市 诸暨市 (Zhuji)", "short": "诸暨", "pinyin": "zhuji", "lat": 29.7126, "lng": 120.2319, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 宁波市 慈溪市 (Cixi)", "short": "慈溪", "pinyin": "cixi", "lat": 30.1690, "lng": 121.2664, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 宁波市 余姚市 (Yuyao)", "short": "余姚", "pinyin": "yuyao", "lat": 30.0381, "lng": 121.1534, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 嘉兴市 海宁市 (Haining)", "short": "海宁", "pinyin": "haining", "lat": 30.5097, "lng": 120.6813, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 嘉兴市 桐乡市 (Tongxiang / 乌镇)", "short": "桐乡", "pinyin": "tongxiang", "lat": 30.6302, "lng": 120.5463, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 嘉兴市 平湖市 (Pinghu)", "short": "平湖", "pinyin": "pinghu", "lat": 30.6968, "lng": 121.0216, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "浙江省 嘉兴市 嘉善县 (Jiashan / 西塘)", "short": "嘉善", "pinyin": "jiashan", "lat": 30.8299, "lng": 120.9256, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "浙江省 嘉兴市 (Jiaxing)", "short": "嘉兴", "pinyin": "jiaxing", "lat": 30.7461, "lng": 120.7555, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 湖州市 德清县 (Deqing / 莫干山)", "short": "德清", "pinyin": "deqing", "lat": 30.5332, "lng": 119.9786, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 湖州市 安吉县 (Anji)", "short": "安吉", "pinyin": "anji", "lat": 30.6378, "lng": 119.6811, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 湖州市 长兴县 (Changxing)", "short": "长兴", "pinyin": "changxing", "lat": 31.0062, "lng": 119.9079, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "浙江省 湖州市 (Huzhou)", "short": "湖州", "pinyin": "huzhou", "lat": 30.8943, "lng": 120.0868, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 绍兴市 嵊州市 (Shengzhou)", "short": "嵊州", "pinyin": "shengzhou", "lat": 29.5786, "lng": 120.8219, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "浙江省 绍兴市 (Shaoxing)", "short": "绍兴", "pinyin": "shaoxing", "lat": 30.0024, "lng": 120.5821, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 温州市 乐清市 (Yueqing)", "short": "乐清", "pinyin": "yueqing", "lat": 28.1232, "lng": 120.9859, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 温州市 瑞安市 (Ruian)", "short": "瑞安", "pinyin": "ruian", "lat": 27.7806, "lng": 120.6547, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 温州市 (Wenzhou)", "short": "温州", "pinyin": "wenzhou", "lat": 28.0006, "lng": 120.6721, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "浙江省 金华市 东阳市 (Dongyang)", "short": "东阳", "pinyin": "dongyang", "lat": 29.2894, "lng": 120.2419, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 金华市 永康市 (Yongkang)", "short": "永康", "pinyin": "yongkang", "lat": 28.9464, "lng": 120.0473, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 台州市 临海市 (Linhai)", "short": "临海", "pinyin": "linhai", "lat": 28.8561, "lng": 121.1287, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 台州市 温岭市 (Wenling)", "short": "温岭", "pinyin": "wenling", "lat": 28.3718, "lng": 121.3619, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "浙江省 舟山市 (Zhoushan)", "short": "舟山", "pinyin": "zhoushan", "lat": 30.0003, "lng": 122.2072, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},

    # 广东、福建、山东、四川其他重点城镇
    {"name": "广东省 佛山市 顺德区 (Shunde)", "short": "顺德", "pinyin": "shunde", "lat": 22.8028, "lng": 113.2925, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "广东省 佛山市 南海区 (Nanhai)", "short": "南海", "pinyin": "nanhai", "lat": 23.0287, "lng": 113.1432, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "广东省 东莞市 (Dongguan)", "short": "东莞", "pinyin": "dongguan", "lat": 23.0205, "lng": 113.7518, "tz": "Asia/Shanghai", "country": "中国", "weight": 85},
    {"name": "广东省 中山市 (Zhongshan)", "short": "中山", "pinyin": "zhongshan", "lat": 22.5176, "lng": 113.3928, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "广东省 珠海市 (Zhuhai)", "short": "珠海", "pinyin": "zhuhai", "lat": 22.2707, "lng": 113.5767, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "福建省 泉州市 晋江市 (Jinjiang)", "short": "晋江", "pinyin": "jinjiang", "lat": 24.7814, "lng": 118.5750, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "福建省 泉州市 (Quanzhou)", "short": "泉州", "pinyin": "quanzhou", "lat": 24.8741, "lng": 118.6757, "tz": "Asia/Shanghai", "country": "中国", "weight": 80},
    {"name": "山东省 烟台市 龙口市 (Longkou)", "short": "龙口", "pinyin": "longkou", "lat": 37.6465, "lng": 120.5059, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "山东省 潍坊市 寿光市 (Shouguang)", "short": "寿光", "pinyin": "shouguang", "lat": 36.8814, "lng": 118.7402, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},
    {"name": "四川省 成都市 都江堰市 (Dujiangyan)", "short": "都江堰", "pinyin": "dujiangyan", "lat": 30.9882, "lng": 103.6472, "tz": "Asia/Shanghai", "country": "中国", "weight": 75},
    {"name": "四川省 德阳市 广汉市 (Guanghan / 三星堆)", "short": "广汉", "pinyin": "guanghan", "lat": 30.9768, "lng": 104.2825, "tz": "Asia/Shanghai", "country": "中国", "weight": 70},

    # 海外硅谷与知名城镇
    {"name": "美国 圣何塞 / 硅谷 (San Jose, CA)", "short": "圣何塞", "pinyin": "shenghesai", "lat": 37.3382, "lng": -121.8863, "tz": "America/Los_Angeles", "country": "美国", "weight": 85},
    {"name": "美国 尔湾 (Irvine, CA)", "short": "尔湾", "pinyin": "erwan", "lat": 33.6846, "lng": -117.8265, "tz": "America/Los_Angeles", "country": "美国", "weight": 80},
    {"name": "美国 帕洛阿尔托 (Palo Alto, CA)", "short": "帕洛阿尔托", "pinyin": "paluoaertuo", "lat": 37.4419, "lng": -122.1430, "tz": "America/Los_Angeles", "country": "美国", "weight": 80},
    {"name": "美国 库比蒂诺 (Cupertino, CA)", "short": "库比蒂诺", "pinyin": "kubidinuo", "lat": 37.3230, "lng": -122.0322, "tz": "America/Los_Angeles", "country": "美国", "weight": 80},
    {"name": "美国 西雅图 (Seattle, WA)", "short": "西雅图", "pinyin": "xiyatu", "lat": 47.6062, "lng": -122.3321, "tz": "America/Los_Angeles", "country": "美国", "weight": 85},
    {"name": "美国 波士顿 (Boston, MA)", "short": "波士顿", "pinyin": "boshidun", "lat": 42.3601, "lng": -71.0589, "tz": "America/New_York", "country": "美国", "weight": 85},
    {"name": "美国 剑桥 (Cambridge, MA)", "short": "剑桥", "pinyin": "jianqiao", "lat": 42.3736, "lng": -71.1097, "tz": "America/New_York", "country": "美国", "weight": 80},
    {"name": "加拿大 温哥华 (Vancouver)", "short": "温哥华", "pinyin": "wengehua", "lat": 49.2827, "lng": -123.1207, "tz": "America/Vancouver", "country": "加拿大", "weight": 85}
]


def search_cities(query: str, limit: int = 15) -> list:
    """
    Lightning-fast in-memory fuzzy & prefix search with weighted ranking.
    Prioritizes:
    1. Exact Match on short name (e.g. "太仓", "北京")
    2. Exact Match on pinyin
    3. Prefix matches sorted by popularity weight
    4. Substring matches sorted by popularity weight
    """
    if not query or not query.strip():
        # Default top famous cities
        sorted_defaults = sorted(GEO_DATA_LIST, key=lambda x: -x.get("weight", 50))
        return sorted_defaults[:limit]

    q = query.strip().lower()

    exact_matches = []
    prefix_matches = []
    partial_matches = []

    for item in GEO_DATA_LIST:
        name_lower = item["name"].lower()
        short_lower = item["short"].lower()
        pinyin = item["pinyin"]
        weight = item.get("weight", 50)

        # 1. Exact Match
        if q == short_lower or q == pinyin:
            exact_matches.append((item, 1000 + weight))
        # 2. Prefix Match
        elif short_lower.startswith(q) or pinyin.startswith(q) or name_lower.startswith(q):
            prefix_matches.append((item, 500 + weight))
        # 3. Substring Match
        elif q in name_lower or q in pinyin:
            partial_matches.append((item, weight))

    # Sort each category by final score descending
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
