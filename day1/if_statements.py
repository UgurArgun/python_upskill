
browser_name = "firefox"

if browser_name == "chrome":
    print("Chrome browser is open")
elif browser_name == "firefox":
    print("Firefox browser is open")
elif browser_name == "safari":
    print("Safari browser is open")
elif browser_name == "edge":
    print("Edge browser is open")
else:
    print("Browser is not supported")

print("--------------------------------------")

# Nested if statement

score = -200

if 0 <= score <= 100:
    if score >= 60:
        print("You have passed the exam")
    else:
        print("You have failed the exam")
else:
    print("Score is not valid")