from models import Dog

def create_table(base,engine):
    #engine = create_engine('sqlite:///dogs.db')
    base.metadata.create_all(engine)
    
def save(session, dog):
    #Session = sessionmaker(bind=engine)
    #session = Session()
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()
    #if use filter(Dog.name==name)
    #or use filter_by(name=name)

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id==id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name,breed=breed).first()

def update_breed(session, dog, breed):
    #for updating bulk session.query(Music).update() for single record update session.query(Music).get(id)
    #return session.query(Dog).update({Dog.breed:breed})
    #return session.query(Dog).get(id)
    dog.breed = breed
    session.commit()
