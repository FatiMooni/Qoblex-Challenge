class NotFoundBundleException(Exception):
    pass

# Bundle is a node in the N-ary tree (product)
class Bundle:
	def __init__(self, name : str,  piece_number : int =1, children = None):
		self.name = name
		self.piece_number = piece_number
		self.children = children or []
	
	def __str__(self):
		return str(self.name)

# Product is group of bundles ( we use N-ary tree structure to represent the product)
class Product:
    # NOTE : add and find are two additional method to build graph
	def __init__(self):
		self.root = None     

	def find(self, bundle : Bundle, key : str) -> Bundle:
		if bundle == None or bundle.name == key:
			return bundle		
		for child in bundle.children:
			found_bundle = self.find(child, key)
			if found_bundle: 
				return found_bundle
		return None		

	def add(self, bundle_name : str, p_num : int =1, parent_key : str = None):
		bundle = Bundle(bundle_name, piece_number=p_num)
		if parent_key == None:
			self.root = bundle
		else:
			parent_bundle = self.find(self.root, parent_key)
			if (not parent_bundle): 
				raise NotFoundBundleException
			parent_bundle.children.append(bundle)
	
    # NOTE : this method is main solution of challenge
    # CHECK README.md for more details about thought process
	def construct(self, root: Bundle, stock ) -> int:
		if root == None:
			return 0
		if len(root.children) == 0: # leaf node
			if root.name not in stock: return 0 # in case the bundle doesn't exist in stock
			
			return stock[root.name] # all pieces can be used by default
		
        # if root is not leaf node
		max_possible_bundles = float('inf')
		for child in root.children:
			max_possible_bundles = min(max_possible_bundles, self.construct(child, stock) // child.piece_number)

		# precaution : in case we loaded a bundle that has no children 	
		return 0 if max_possible_bundles == float('inf') else max_possible_bundles
			


if __name__ == "__main__":
    # example 1			
	bike = Product()
	bike.add("bike")
	bike.add("wheel", 2, "bike")
	bike.add("seat", 1, "bike")
	bike.add("pedal", 2, "bike")
	bike.add("tube", 1, "wheel")
	bike.add("frame", 1, "wheel")

	stock = {
	    "seat" : 50,
	    "pedal" : 60,
	    "frame" : 60,
	    "tube" : 35
	}


	print("number of bikes : " , bike.construct(bike.root, stock))

	# example 2
	# p0 = Product()
	# p0.add('p0')
	# p0.add('p1', 2, "p0")
	# p0.add('p2', 4, "p0")
	# p0.add('p3', 1, "p0")
	# p0.add('p4', 3, "p0")
	# p0.add('p1a', 2, "p1")
	# p0.add('p1b', 4, "p1")
	# p0.add('p1c', 3, "p1")
	# p0.add('p2a', 1, "p2")
	# p0.add('p2b', 1, "p2")
	# p0.add('p4a', 1, "p4")
	# p0.add('p4a*', 1, "p4a")

	# stock = {
	#     "p3" : 50,
	#     "p1a" : 60,
	#     "p1b" : 86,
	#     "p1c" : 48,
	# 	"p2a" : 60,
	#     "p2b" : 60,
	#     "p4a*" : 9,
	# }


	# print("number of P0 : " , p0.construct(p0.root, stock))



	