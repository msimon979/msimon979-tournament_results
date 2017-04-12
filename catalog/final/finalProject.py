from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

def restName(restaurant_id):
    restId = restaurant_id - 1
    restaurant = restaurants[restId]['name']
    return restaurant

def restId(restaurant_id):
    restId = restaurant_id - 1
    return restId

@app.route('/restaurants/JSON')
def restaurantJSON():
    return jsonify(results = restaurants)

@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def menuJSON(restaurant_id):
    r_id = restId(restaurant_id)
    return jsonify( results = items[r_id])

@app.route('/')
@app.route('/restaurant')
def showRestaurants():
    return render_template('restaurants.html', restaurants = restaurants)


@app.route('/restaurant/new')
def newRestaurant():
    return render_template('newrestaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    if restaurant_id >= 3:
        return redirect(url_for('showRestaurants'))
    else:
        restaurant = restName(restaurant_id)
        return render_template('editrestaurant.html', restaurant = restaurant)

@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    if restaurant_id >= 3:
        return redirect(url_for('showRestaurants'))
    else:
        restaurant = restName(restaurant_id)
        return render_template('deleterestaurant.html', restaurant = restaurant)

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    r_id = restId(restaurant_id)
    r_name = restName(restaurant_id)
    return render_template('menu.html', restaurant_id = r_id, restaurant_name = r_name, item = items)

@app.route('/restaurant/restaurant/menu/new')
def newMenuItem():
    return "This page is for making a new menu item for restaurant %s" % restaurant_id

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id,menu_id):
    return "This page is for editing menu item %s" % menu_id

@app.route('/restaurant/restaurant_id/menu/menu_id/delete')
def deleteMenuItem():
    return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)