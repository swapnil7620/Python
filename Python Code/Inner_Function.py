
# function inside the other function is called inner function
def greet():
      def message(n):
            print("welcome",n)
      return message


result = greet()
result(5)
