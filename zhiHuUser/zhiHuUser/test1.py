import redis
import pickle
pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    for i in r.sscan_iter("zhiHuUser3"):
        print(pickle.loads(i))