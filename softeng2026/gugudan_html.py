dan = 5

filename = "gugudan.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"<html>")
    f.write(f"<head><title>gugudan {dan}</title></head><body>")
    f.write(f"<h1>gugudan {dan}</h1>")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
        f.write(f"<p>{dan} x {i} = <font color='green'>{dan * i}</font></p>")
    f.write("</body></html>")