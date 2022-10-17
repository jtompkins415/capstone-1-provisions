from models import db, User, Beer, Brewery, Wine, Winery, Food
from app import app

db.drop_all()
db.create_all()

##USERS

rachel = User("rachelgurl235", "rachel.adams916@gmail.com", "Rachel", "Adams", "password1", "Sacramento", "CA")
doug = User("superdrinker34", "douggydogg@gmail.com", "Doug", "Jones", "password2", "Los Angeles", "CA")
felix = User("felixthecat233", "felixthecat@yahoo.com", "Felix", "Bower", "password3", "New Orleans", "LA")
gina = User("winelover98", "gina.rochelle40@aol.com", "Gina", "Harrison", "password4", "Salt Lake City", "UT")
morgan = User("runandchug32", "morgan.dunnigan@hotmail.com", "Morgan", "Dunnigan", "password5", "Burmingham", "AL")
lewis = User("lewisbiggulp60", "lewis.killigan@gmail.com", "Lewis", "Killigan", "password6", "Seattle", "WA")

db.session.add_all([rachel, doug, felix, gina, morgan, lewis])
db.session.commit()

##BEER

delirium = Beer('Delirium Tremens', 'Brouwerij Huyghe', 'Belgian Golden Ale', 8.99, 8.5, 'Belgian fruit and spice notes, light gold color, smooth drinking for a higher abv beer, voted world`s best beer')
pliny = Beer('Pliny the Elder', 'Russian River', 'DIPA', 8.00, 8.5, 'The cult classic from Russian River! Solid malt backbone supports fresh hop flavors')
dupont = Beer('Saison Dupont', 'Brasserie Dupont','Belgian Farmhouse Ale', 6.99, 6.5, 'Coppery blond, the finest aromas and a strong bitterness transform this beer into a thirst-quenchener with no equal, just the way it was created. Dupont`s selection of yeasts is the perfect base for these typical aromas and ditto taste. A real refermentation in the bottle, which will continue for a long time in your cellar, result into this complex and particular aromatic beer.')
ten_degrees = Beer('10 Degrees', 'Urban Roots Brewing','Czech Style Lager', 5.99, 3.9, 'Czech Style served in a Czech style beer glass and from a traditional “side pull” tap handle for a truly authentic experience. This beer is brewed with 100% Czech grown Saaz hops and floor malted Bohemian Pilsner malt made just outside of Prague (thanks to Weyermann Specialty Malts) which lends it plenty of richness and complexity with a classic hop flavor and aroma')
righteo = Beer('Righteo', 'Original Pattern', 'Hazy Pale Ale', 6.49, 5.6, 'NZ Rakau, NZ Moutere, and Mosaic hops create flavorful notes of apricot, grapefruit, and pine that pair beautifully with a medium, pillowy body, and low-to-no hop bitterness.')
orval = Beer('Orval', 'Brasserie d`Orval', 'Trappist Ale', 8.00, 6.9, ' Orval is brewed unfiltered by Catholic monks at a monastery founded in the 1100s in the pastoral Belgium countryside. Three different malts and two types of hops, & Brettanomyces yeast, impart a great character and complexity.' )

db.session.add_all([delirium, pliny, dupont, ten_degrees, righteo, orval])
db.session.commit()

##BREWERIES

huyghe = Brewery("Brouwerij Huyghe", 'Melle', 'East Flanders', 'Belgium', 1)
russian_river = Brewery('Russian River', 'Windsor', 'CA', 'United States', 2)
brass_dupont = Brewery('Brasserie Dupont', 'Tourpes', 'Hainaut', 'Belgium', 3)
urb_roots = Brewery('Urban Roots Brewing', 'Sacramento', 'CA', 'United States', 4)
og_pattern = Brewery('Original Pattern', 'Oakland', 'CA', 'United States', 5)
brass_orval = Brewery('Brasserie d`Orval', 'Florenville', 'Luxembourg', 'Belgium', 6)

db.session.add_all([huyghe, russian_river, brass_dupont, urb_roots, og_pattern, brass_orval])
db.session.commit()

