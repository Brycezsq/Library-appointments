
from selenium import webdriver
import time
# 用selenium打开网页
from selenium.webdriver.common.by import By


def openPage():
    driver = webdriver.Chrome(executable_path=r"D:\chromedriver.exe")
    driver.get("http://dj.ggwhy.cn:8033/#/index?orga=dltq")
    time.sleep(2)
    driver.find_element_by_css_selector('img[src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAC7UlEQVRYR+2YTUhUURTHf38lbFGNY9LHorCQiIqSWpVBBS5s1SYIahkR5AdCSR+biqJFJJHlhKs2LYvatGpRRGAtCgpEKlLoY5M0aUQQoifum/fGN+PofA8K3tXMe/ec83v/c859910xz4fmOR+LgMVmaGEraGY7gRXFqpDFPi7p/WxzZihoZjXANeAosKbMcIH778ATSSfT46UAmlkDMFIhqIxhJKUwpQM+BVp8S/c0jySNlhPYzOqATuCiH6dH0pkgZhLQzDYBH/wblyVdKidYum8zOwbc96+vCoQJA4YnrJP0rcKA4fLaJemtix8GdIp5MqfXQaVAzcz8WAckPZ8dkPEYTMbQysGKwFm8Gaq6jMjhXAGdjv+AGEz0oHq3DJR+2M8tUN0FnHDOjUgQI6uCbqnZ4M/+nQCNXEH6WxJKG10LSxxYd6jMho3IxhwVjK+H6jbgFLA8YeQtNzEUKby7bWQpRLvAzoJqQwL0uZIy6r7mBhgslvanCSbaQcenlTOX7h4UvZmXmjbm1tVzgOvWYPSD3UXRd16Kc26StNUcG2sBc6CHQs6Hwa6i6L05QW3siA/WFJr3EKwPRZ+FbQsHDLx4wdQOtjfkeAjsAoo+TgG18VYwp9i+0PUXwG1U+yDTQxUPmASNt0G1A908HUivYOp84n+Vq7Ow2kPALVTbP5fapQP0CuaXK/JOUAdQnzmw11i9MHUHRcey1WxpAZNq/miEmg4w98IPDesFOdWGs4ElXRXcJLlESCjaADYJfEF147mYlbZJ8o2Y5/zypDhPiMo1SQnBKlODJQBeTHGxIi54BfcDwct7j6SBYhXJx97MmoGXvk2jpM/ud/ibxO37PgGrgUFJ2/IJUOxcM3PiOJE+Atslb0eferplZtf9Xa679wZ4DZT1uxhYBrQCW/2HTG73ZwB6ewCz08CNYhUp0L5bUkrsjKdbZrYDOAjsrsThkV/7A5Jc1lLGwj5+KzBNJTVbVLBYOee9gv8BYW5fOMfyaRgAAAAASUVORK5CYII="]').click()
    time.sleep(5)
    button = driver.find_element_by_xpath(".//*[text()='预约']/..").click()
    print(button.text)

openPage()