from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='dmoitim', email='dmoitim@gmail.com', password='secret'
        )

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'dmoitim'))

        assert asdict(user) == {
            'id': 1,
            'username': 'dmoitim',
            'email': 'dmoitim@gmail.com',
            'password': 'secret',
            'created_at': time,
        }
