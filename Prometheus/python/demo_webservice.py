from flask import Flask
from prometheus_client import Counter, Gauge, Histogram, generate_latest
from prometheus_client import multiprocess, CollectorRegistry
import time
import random

app = Flask(__name__)

# 设置一个请求计数器
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests')
# 设置一个请求处理时间的直方图
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Histogram of request processing latency')

# 模拟一个业务的Gauge指标，比如当前在线用户数
ACTIVE_USERS = Gauge('app_active_users', 'Number of active users')

@app.route('/')
def home():
    # 模拟处理时间
    start_time = time.time()
    REQUEST_COUNT.inc()  # 请求计数器 +1
    ACTIVE_USERS.set(random.randint(1, 10))  # 设置活跃用户数为1到10之间的随机数
    
    # 模拟一些工作负载
    time.sleep(random.uniform(0.1, 0.5))
    
    latency = time.time() - start_time
    REQUEST_LATENCY.observe(latency)  # 记录延迟
    return "Hello, Prometheus!"

@app.route('/metrics')
def metrics():
    # 生成符合 Prometheus 格式的指标数据
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    return generate_latest(registry), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)