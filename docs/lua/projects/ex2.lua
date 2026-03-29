myprint = function(param)
   print("这是打印函数 -   ##",param,"##")
end

function add(num1,num2,functionPrint)
   result = num1 + num2
   -- 调用传递的函数参数
   functionPrint(result)
end
myprint(10)						-->这是打印函数 -   ##	10	##
-- myprint 函数作为参数传递
add(2,5,myprint)				-->这是打印函数 -   ##	7	##
