from app.models.movement import Movement

def test_movement_to_dict_method():
    movement = Movement(
        name='Dance',
        slug='dance',
        category='cardio',
        is_outdoor=False
    )

    movement_dict = movement.to_dict()
    
    assert type(movement_dict) == dict
    assert movement_dict == {
        'id': None,
        'name': 'Dance',
        'slug': 'dance',
        'category': 'cardio',
        'is_outdoor': False
    }