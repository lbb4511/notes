-- 初始化数组
array = {}
for i=1,3 do
   array[i] = {}
      for j=1,3 do
         array[i][j] = i*j
      end
end

-- 访问数组
for i=1,3 do
   for j=1,3 do
      print(array[i][j])	-->1
							-->2
							-->3
							-->2
							-->4
							-->6
							-->3
							-->6
							-->9
   end
end
