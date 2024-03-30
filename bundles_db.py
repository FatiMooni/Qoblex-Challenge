from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
# to load bundles from our DB , we use SQLAlchemy ( python ORM)
class Bundle(Base): # entity class need to implement Base
	
	id = Column(String, primary_key=True)
	name = Column(String)
	## load sub bundles by left join on "parent_bundle_id"
	children = relationship("BundlePieces", back_populates="bundle", foreign_keys=["parent_bundle_id"])

	def __init__(self, name : str,  piece_number : int =1, children = None):
		self.name = name
		self.piece_number = piece_number
		self.children = children or []
	
	def __str__(self):
		return str(self.name)

# Product is group of bundles ( we use N-ary tree structure to represent the product)
class Product:

	def __init__(self , root):
		self.root = root     
	
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
			# pass child.baundle
			max_possible_bundles = min(max_possible_bundles, self.construct(child.bundle, stock) // child.piece_number)
			
		return max_possible_bundles 
			


if __name__ == "__main__":
	engine = create_engine('sqlite:///random_databse.db') 
	Session = sessionmaker(bind=engine)
	session = Session()
	
    # fetch the required bundle (P0) using id or name
	existing_bundle = session.query(Bundle).filter_by(id='bike_bundle_id').first()
	
    # create product 
	# NOTE : since while loading bundle we gonna load all its sub-bundles ( BundlePoices ) there is no need to add pieces one by one
	bike = Product(existing_bundle)
    				

    # stock structure, can be replaced with an array of entity Stock
	stock = {
	    "seat" : 50,
	    "pedal" : 60,
	    "frame" : 60,
	    "tube" : 35
	}
	
	print("number of bikes : " , bike.construct(bike.root, stock))

	