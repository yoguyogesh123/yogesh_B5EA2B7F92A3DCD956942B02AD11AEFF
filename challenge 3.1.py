def linearsearchproduct(productlist,targetproduct):
  indices = []

  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices
#example usage:
product = ["shoes","boot","loofer","shoes","sandal","shoes"]
target = "shoes"
target2 = "apple"
result = linearsearchproduct(product,target)
print(result)