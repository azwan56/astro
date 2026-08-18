# 零付费 API 纯开源人类图 (Human Design) 计算引擎 & API 服务

一套完全**零外部付费 API 依赖**、纯本地运行的 Python 人类图排盘与 BodyGraph SVG 矢量图渲染服务。

## 🌟 核心特色
1. **0 外部付费 API 依赖**：本地使用 `ephem` 与星历库完成 13 颗天体黄道经度计算及出生前 $88^\circ$ 太阳弧（Design 端）倒推。
2. **极速 315° Mandala 映射算法**：无缝换算天体黄经至 64 卦门与 384 爻线。
3. **完全内在权威判定树 (Authority Hierarchy)**：自动判断反映者、显能者、生产者、显能生产者、投影者，以及情绪、荐骨、直觉、意志力、自我投影、心智/环境和月亮权威。
4. **原生 BodyGraph SVG 动态生成**：后端直接生成响应式矢量 SVG，可直接上云 CDN 或直接渲染于微信小程序/前端。
5. **离线全球时区解析**：基于 `timezonefinder` 离线根据经纬度自动处理历史夏令时 (DST) 及 UTC 转换。

## 📁 目录结构
```
/Users/azwan/Projects/astro/
├── app/
│   ├── main.py                # FastAPI 路由入口
│   ├── core/
│   │   ├── ephemeris.py       # 天体星历与 88° 太阳弧算法
│   │   ├── mandala.py         # 315° 黄道卦门爻线转换器
│   │   ├── authority_tree.py  # 能量类型与内在权威判定树
│   │   └── svg_render.py      # BodyGraph SVG 动态绘图器
│   ├── data/
│   │   └── hd_topology.py     # 9中心 64卦门 36通道静态拓扑
│   ├── db/
│   │   └── coach_texts.json   # 教练释义文案数据库
│   └── schemas/
│       └── hd_models.py       # Pydantic 接口请求响应数据模型
├── tests/
│   └── test_engine.py         # 单元测试
├── Dockerfile                 # 容器化部署文件
├── requirements.txt           # Python 依赖清单
└── README.md                  # 说明文档
```

## 🚀 本地快速启动

### 1. 安装依赖
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 启动服务
```bash
uvicorn app.main:app --reload --port 8000
```
访问 API 文档：`http://localhost:8000/docs`

### 3. API 请求示例
`POST /api/v1/chart/calculate`
```json
{
  "birth_date": "1990-06-15",
  "birth_time": "14:30",
  "latitude": 31.2304,
  "longitude": 121.4737,
  "timezone_str": "Asia/Shanghai"
}
```

## 🐳 Docker 部署 (阿里云 FC / Serverless / ECS)
```bash
docker build -t humandesign-api:latest .
docker run -p 8000:8000 humandesign-api:latest
```
