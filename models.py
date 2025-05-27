from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class DriverMaster(db.Model):
    __tablename__ = 'driver_master'
    driver_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    license_no = db.Column(db.String)
    contact = db.Column(db.String)
    address = db.Column(db.String)
    availability = db.Column(db.String)
    shift = db.Column(db.String)
    aadhar = db.Column(db.String)
    license = db.Column(db.String)

    fleet_vehicles = db.relationship('Fleet', back_populates='driver')


class Fleet(db.Model):
    __tablename__ = 'fleet'
    vehicle_id = db.Column(db.String, primary_key=True)
    vehicle_name = db.Column(db.String)
    assigned_driver_id = db.Column(db.String, db.ForeignKey('driver_master.driver_id'))
    model = db.Column(db.String)
    capacity_wei = db.Column(db.Float)
    capacity_vol = db.Column(db.Float)
    documents_expiry = db.Column(db.Date)
    actions = db.Column(db.String)

    driver = db.relationship('DriverMaster', back_populates='fleet_vehicles')
    orders = db.relationship('Order', back_populates='fleet_vehicle')


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.String, primary_key=True)
    customer_name = db.Column(db.String)
    order_type = db.Column(db.String)
    pickup_location_latlon = db.Column(db.String)
    drop_location_latlon = db.Column(db.String)
    volume = db.Column(db.Float)
    weight = db.Column(db.Float)
    priority = db.Column(db.String)
    expected = db.Column(db.Date)
    status = db.Column(db.String)
    vehicle_id = db.Column(db.String, db.ForeignKey('fleet.vehicle_id'))

    fleet_vehicle = db.relationship('Fleet', back_populates='orders')

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.String(100), db.ForeignKey('vehicles.vehicle_id'))  # foreign key here
    driver = db.Column(db.String(100))
    orders = db.Column(db.Text)




