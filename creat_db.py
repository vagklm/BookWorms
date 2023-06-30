import sqlite3


# Create the database and table if they don't exist
def create_database():
    try:
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        
        # Create the 'books' table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        price REAL,
                        description TEXT
                    )''')
        # Commit the changes and close the connection
        connection.commit()
        connection.close()
    # Raise an error if connection fails
    except sqlite3.Error as error:
        print("Error while connecting to sqlite database", error)
        
# Insert books in the database
def add_books():
    try:
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        
        # Adding books to the database
        books = [
            ("Metro 2033", "Glukhovsky Dmitry", "12.52", "Metro 2033 tells the story of a young man named Artyom who goes a long way to save his world from mortal danger. The book describes the consequences of an atomic war. Its only survivors strive for existence in the mazes of the Moscow subway (Metro) some two decades after the nuclear Holocaust. Formally a sci-fi novel, Metro 2033 describes a dystopia, in which Russia's present-day society is superficially analyzed and described. It also critically examines communism in the former Soviet Union and the rise of fascism in modern Russia. Over 2,000,000 copies of Metro 2033 have been sold worldwide. Foreign book rights have been sold to more than 37 countries. The franchise gave birth to two cult video games, Metro 2033 and Metro Last Light. Film rights were optioned by MGM Studios in Hollywood."),
            ("Dune", "Frank Herbert", "10.52", "Before The Matrix, before Star Wars, before Ender's Game and Neuromancer, there was Dune: winner of the prestigious Hugo and Nebula awards, and widely considered one of the greatest science fiction novels ever written.Melange, or 'spice', is the most valuable - and rarest - element in the universe; a drug that does everything from increasing a person's life-span to making interstellar travel possible. And it can only be found on a single planet: the inhospitable desert world Arrakis.Whoever controls Arrakis controls the spice. And whoever controls the spice controls the universe.When the Emperor transfers stewardship of Arrakis from the noble House Harkonnen to House Atreides, the Harkonnens fight back, murdering Duke Leto Atreides. Paul, his son, and Lady Jessica, his concubine, flee into the desert. On the point of death, they are rescued by a band for Fremen, the native people of Arrakis, who control Arrakis' second great resource: the giant worms that burrow beneath the burning desert sands.In order to avenge his father and retake Arrakis from the Harkonnens, Paul must earn the trust of the Fremen and lead a tiny army against the innumerable forces aligned against them.And his journey will change the universe."),
            ("The Lord Of The Rings: The Fellowship Of The Ring", "Tolkien J.R.R", "10.74", "Continuing the story begun in The Hobbit, this is the first part of Tolkien's epic masterpiece, The Lord of the Rings, featuring a striking black cover based on Tolkien's own design, the definitive text, and a detailed map of Middle-earth.Sauron, the Dark Lord, has gathered to him all the Rings of Power - the means by which he intends to rule Middle-earth. All he lacks in his plans for dominion is the One Ring - the ring that rules them all - which has fallen into the hands of the hobbit, Bilbo Baggins.In a sleepy village in the Shire, young Frodo Baggins finds himself faced with an immense task, as his elderly cousin Bilbo entrusts the Ring to his care. Frodo must leave his home and make a perilous journey across Middle-earth to the Cracks of Doom, there to destroy the Ring and foil the Dark Lord in his evil purpose.Now published again in B format, J.R.R. Tolkien's great work of imaginative fiction has been labelled both a heroic romance and a classic fantasy fiction. By turns comic and homely, epic and diabolic, the narrative moves through countless changes of scene and character in an imaginary world which is totally convincing in its detail."),
            ("1984", "George Orwell", "10.79", "The perfect edition for any Orwell enthusiasts' collection, discover the classic dystopian masterpiece beautifully reimagined by renowned street artist Shepard FaireyWinston Smith works for the Ministry of Truth in London, chief city of Airstrip One. Big Brother stares out from every poster, the Thought Police uncover every act of betrayal. When Winston finds love with Julia, he discovers that life does not have to be dull and deadening, and awakens to new possibilities. Despite the police helicopters that hover and circle overhead, Winston and Julia begin to question the Party; they are drawn towards conspiracy. Yet Big Brother will not tolerate dissent - even in the mind. For those with original thoughts they invented Room 101. . . First published in 1949, 1984 is George Orwell's terrifying vision of a totalitarian future in which everything and everyone is slave to a tyrannical regime."),
            ("Neuromancer", "William Gibson", "12.59", "The book that defined the cyberpunk movement, inspiring everything from The Matrix to Cyberpunk 2077.The sky above the port was the colour of television, tuned to a dead channel.William Gibson revolutionised science fiction in his 1984 debut Neuromancer. The writer who gave us the matrix and coined the term 'cyberspace' produced a first novel that won the Hugo, Nebula and Philip K. Dick Awards, and lit the fuse on the Cyberpunk movement.More than three decades later, Gibson's text is as stylish as ever, his noir narrative still glitters like chrome in the shadows and his depictions of the rise and abuse of corporate power look more prescient every day. Part thriller, part warning, Neuromancer is a timeless classic of modern SF and one of the 20th century's most potent and compelling visions of the future. His later work, The Peripheral, has been adapted into a series by Amazon Prime, starring Chloe Grace Moretz."),
            ("Don Quixote", "Miguel de Cervantes", "4.11", "Translated by P. A. Motteux With an Introduction and Notes by Stephen Boyd, University College, Cork Cervantes' tale of the deranged gentleman who turns knight-errant, tilts at windmills and battles with sheep in the service of the lady of his dreams, Dulcinea del Toboso, has fascinated generations of readers, and inspired other creative artists such as Flaubert, Picasso and Richard Strauss. The tall, thin knight and his short, fat squire, Sancho Panza, have found their way into films, cartoons and even computer games. Supposedly intended as a parody of the most popular escapist fiction of the day, the 'books of chivalry', this precursor of the modern novel broadened and deepened into a sophisticated, comic account of the contradictions of human nature. On his 'heroic' journey Don Quixote meets characters of every class and condition, from the prostitute Maritornes, who is commended for her Christian charity, to the Knight of the Green Coat, who seems to embody some of the constraints of virtue. Cervantes' greatest work can be enjoyed on many levels, all suffused with a subtle irony that reaches out to encompass the reader, and does not leave the author outside its circle. Peter Motteux's fine eighteenth-century translation, acknowledged as one of the best, brilliantly succeeds in communicating the spirit of the original Spanish."),
            ("Hamlet", "William Shakespeare", "5.47", "Edited, Introduced and Annotated by Cedric Watts, M.A., Ph.D., Emeritus Professor of English, University of Sussex. The Wordsworth Classics' Shakespeare Series presents a newly-edited sequence of William Shakespeare's works. The Textual editing takes account of recent scholarship while giving the material a careful reappraisal. Hamlet is not only one of Shakespeare's greatest plays, but also the most fascinatingly problematical tragedy in world literature. First performed around 1600, this a gripping and exuberant drama of revenge, rich in contrasts and conflicts. Its violence alternates with introspection, its melancholy with humour, and its subtlety with spectacle. The Prince, Hamlet himself, is depicted as a complex, divided, introspective character. His reflections on death, morality and the very status of human beings make him 'the first modern man'. Countless stage productions and numerous adaptations for the cinema and television have demonstrated the continuing cultural relevance of this vivid, enigmatic, profound and engrossing drama."),
            ("The Odyssey", "Homer", "4.29", "HarperCollins is proud to present its new range of best-loved, essential classics. `Alas that mortals Should blame the gods! From us, they say, All evils come. Yet they themselves It is who through defiant deeds Bring sorrow on them-far more sorrow Than fate would have them bear.' Attributed to the blind Greek poet, Homer, The Odyssey is an epic tale about cunning and strength of mind. It takes its starting point ten years after the fall of the city of Troy and follows its Greek warrior hero Odysseus as he tries to journey to his home of Ithaca in northwest Greece after the Greek victory over the Trojans. On his travels, Odysseus comes across surreal islands and foreign lands where he is in turn challenged and supported by those that he meets on his travels as he attempts to find his way back home in order to vanquish those who threaten his estate. In turn, his son Telemachus has to grow up quickly as he attempts to find his father and protect his mother from her suitors. Dealing with the universal themes of temptation and courage, the epic journey that Odysseus undertakes is as meaningful today as it was almost 3,000 years ago when the story was composed."),
            ("The Brothers Karamazov", "Fyodor Dostoyevsky", "10.63", "'The most magnificent novel ever written' Sigmund Freud The murder of brutal landowner Fyodor Karamazov changes the lives of his sons irrevocably: Mitya, the sensualist, whose bitter rivalry with his father immediately places him under suspicion for parricide; Ivan, the intellectual, driven to breakdown; the spiritual Alyosha, who tries to heal the family's rifts; and the shadowy figure of their bastard half-brother, Smerdyakov. Dostoyevsky's dark masterwork evokes a world where the lines between innocence and corruption, good and evil, blur, and everyone's faith in humanity is tested. Translated with an Introduction and notes by DAVID McDUFF"),
            ("Les Miserables", "Victor Hugo", "23.99", "'So long as ignorance and poverty exist on earth, books of the nature of Les Miserables cannot fail to be of use,' says Victor Hugo in the preface of his famous novel. Certainly, Les Miserables is French history recounted through the personal stories of its main characters. The tale offers philosophical insight on the good deeds that can happen even amid ignorance and poverty. This handsome leather-bound volume is a beautiful addition to any classic literature library with specially designed endpapers, gilded edges, and a ribbon bookmark so you never lose your place.")
            ]
        
        cursor.executemany('INSERT INTO books (title, author, price, description) VALUES (?, ?, ?, ?)', books)
        
        # Commit the changes to the database and close the connection
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite database", error)
        
# Call the functions to create the database
create_database()
add_books()