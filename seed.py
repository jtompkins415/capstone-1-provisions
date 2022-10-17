from models import User, Beer, Brewery, Wine, Winery, Food
from app import db

db.drop_all()
db.create_all()

##USERS

rachel = User(username="rachelgurl235", email="rachel.adams916@gmail.com", first_name="Rachel", last_name="Adams", password="password1", user_city="Sacramento", user_state="CA")
doug = User(username="superdrinker34", email="douggydogg@gmail.com", first_name="Doug", last_name="Jones", password="password2", user_city="Los Angeles", user_state= "CA")
felix = User(username="felixthecat233", email="felixthecat@yahoo.com", first_name="Felix", last_name="Bower", password="password3", user_city="New Orleans", user_state="LA")
gina = User(username="winelover98", email="gina.rochelle40@aol.com", first_name="Gina", last_name="Harrison", password="password4", user_city="Salt Lake City", user_state="UT")
morgan = User(username="runandchug32", email="morgan.dunnigan@hotmail.com", first_name="Morgan", last_name="Dunnigan", password="password5", user_city="Burmingham", user_state="AL")
lewis = User(username="lewisbiggulp60", email="lewis.killigan@gmail.com", first_name="Lewis", last_name="Killigan", password="password6", user_city="Seattle", user_state="WA")

db.session.add_all([rachel, doug, felix, gina, morgan, lewis])
db.session.commit()

##BEER

delirium = Beer(beer_name='Delirium Tremens', brewery='Brouwerij Huyghe', style='Belgian Golden Ale', price=8.99, abv=8.5, description='Belgian fruit and spice notes, light gold color, smooth drinking for a higher abv beer, voted world`s best beer')
pliny = Beer(beer_name='Pliny the Elder', brewery='Russian River', style='DIPA', price=8.00, abv=8.5, description='The cult classic from Russian River! Solid malt backbone supports fresh hop flavors')
dupont = Beer(beer_name='Saison Dupont', brewery='Brasserie Dupont', style='Belgian Farmhouse Ale', price=6.99, abv=6.5, description='Coppery blond, the finest aromas and a strong bitterness transform this beer into a thirst-quenchener with no equal, just the way it was created. Dupont`s selection of yeasts is the perfect base for these typical aromas and ditto taste. A real refermentation in the bottle, which will continue for a long time in your cellar, result into this complex and particular aromatic beer.')
ten_degrees = Beer(beer_name='10 Degrees', brewery='Urban Roots Brewing', style='Czech Style Lager', price=5.99, abv=3.9, description='Czech Style served in a Czech style beer glass and from a traditional “side pull” tap handle for a truly authentic experience. This beer is brewed with 100% Czech grown Saaz hops and floor malted Bohemian Pilsner malt made just outside of Prague (thanks to Weyermann Specialty Malts) which lends it plenty of richness and complexity with a classic hop flavor and aroma')
righteo = Beer(beer_name='Righteo', brewery='Original Pattern', style='Hazy Pale Ale', price=6.49, abv=5.6, description='NZ Rakau, NZ Moutere, and Mosaic hops create flavorful notes of apricot, grapefruit, and pine that pair beautifully with a medium, pillowy body, and low-to-no hop bitterness.')
orval = Beer(beer_name='Orval', brewery='Brasserie d`Orval', style='Trappist Ale', price=8.00, abv=6.9, description=' Orval is brewed unfiltered by Catholic monks at a monastery founded in the 1100s in the pastoral Belgium countryside. Three different malts and two types of hops, & Brettanomyces yeast, impart a great character and complexity.' )

db.session.add_all([delirium, pliny, dupont, ten_degrees, righteo, orval])
db.session.commit()

##BREWERIES

huyghe = Brewery(brewery_name="Brouwerij Huyghe", city='Melle', state='East Flanders', country='Belgium', beers=1)
russian_river = Brewery(brewery_name='Russian River', city='Windsor', state='CA', country='United States', beers=2)
brass_dupont = Brewery(brewery_name='Brasserie Dupont', city='Tourpes', state='Hainaut', country='Belgium', beers=3)
urb_roots = Brewery(brewery_name='Urban Roots Brewing', city='Sacramento', state='CA', country='United States', beers=4)
og_pattern = Brewery(brewery_name='Original Pattern', city='Oakland', state='CA', country='United States', beers=5)
brass_orval = Brewery(brewer_name='Brasserie d`Orval', city='Florenville', state='Luxembourg', country='Belgium', beers=6)

db.session.add_all([huyghe, russian_river, brass_dupont, urb_roots, og_pattern, brass_orval])
db.session.commit()

