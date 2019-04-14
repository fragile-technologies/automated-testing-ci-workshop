from src.car import Car

def test_car_on_when_engine_on(mocker):
    # Set up mock / given
    engine = mocker.Mock()
    engine.on = True
    car = Car(engine)

    # Get result / when
    actual = car.is_on()
    
    # Assert / then
    assert actual == True

def test_engine_turned_off_when_car_is(mocker):
    # Set up mock / given
    engine = mocker.Mock()
    car = Car(engine)

    # when
    car.turn_off()

    # then assert the function was called once
    engine.turn_off.assert_called_once()