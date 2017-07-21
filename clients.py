from celery import Celery

app = Celery("clients", broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


@app.task(name="test.hello",bind=True)
def f(self):
    print("ok")


a = app.send_task('test.hello')
print(a.get())

print(f.apply_async().get())