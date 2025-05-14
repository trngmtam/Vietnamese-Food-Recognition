import sqlite3

def create_database():
    conn = sqlite3.connect('calories.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS dish_info (
                    dish_name TEXT,
                    ingredient TEXT,
                    weight INTEGER,
                    calories INTEGER,
                    notes TEXT
                )''')

    c.execute('DELETE FROM dish_info')

    pho_data = [
        ('Pho', 'Rice noodles', 175, 215, 'High in carbs'),
        ('Pho', 'Beef (brisket/steak)', 85, 150, 'Leaner cuts vary'),
        ('Pho', 'Broth (beef stock)', 425, 45, 'From simmered bones, some fat'),
        ('Pho', 'Bean sprouts', 40, 8, 'Very low cal'),
        ('Pho', 'Herbs & onion', 15, 4, 'Basil, cilantro, scallion'),
        ('Pho', 'Lime wedge', 5, 1, 'Optional')
    ]

    banhmi_data = [
        ('Banh Mi', 'Baguette', 120, 310, 'High in carbs'),
        ('Banh Mi', 'Pork', 60, 170, 'Grilled or steamed'),
        ('Banh Mi', 'Pickled veggies', 30, 15, 'Carrot, daikon'),
        ('Banh Mi', 'Cucumber', 20, 5, ''),
        ('Banh Mi', 'Cilantro & chili', 5, 2, ''),
        ('Banh Mi', 'Mayonnaise', 15, 100, '')
    ]

    banhxeo_data = [
        ('Banh Xeo', 'Rice flour batter', 150, 260, 'Made with coconut milk'),
        ('Banh Xeo', 'Pork', 50, 140, 'Sliced'),
        ('Banh Xeo', 'Shrimp', 40, 50, 'Medium-sized'),
        ('Banh Xeo', 'Mung beans', 30, 90, 'Steamed'),
        ('Banh Xeo', 'Bean sprouts', 50, 10, 'Low cal'),
        ('Banh Xeo', 'Herbs & lettuce', 20, 5, 'Basil, mint, lettuce')
    ]

    comtam_data = [
        ('Com Tam', 'Broken rice', 200, 260, 'High in carbs'),
        ('Com Tam', 'Grilled pork chop', 120, 340, 'Marinated'),
        ('Com Tam', 'Shredded pork skin', 50, 100, 'With toasted rice powder'),
        ('Com Tam', 'Steamed egg meatloaf', 80, 170, 'Egg, ground pork, glass noodles'),
        ('Com Tam', 'Pickled veggies', 30, 15, ''),
        ('Com Tam', 'Fish sauce dip', 30, 45, 'Sweet-savory')
    ]

    goicuon_data = [
        ('Goi Cuon', 'Rice paper', 20, 35, 'Thin wrapper'),
        ('Goi Cuon', 'Shrimp', 50, 60, 'Boiled'),
        ('Goi Cuon', 'Pork belly', 50, 180, 'Boiled and sliced'),
        ('Goi Cuon', 'Vermicelli noodles', 60, 90, 'Soft rice noodles'),
        ('Goi Cuon', 'Herbs & lettuce', 30, 6, 'Mint, basil, lettuce'),
        ('Goi Cuon', 'Peanut hoisin sauce', 30, 100, 'Sweet-savory')
    ]

    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", pho_data)
    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", banhmi_data)
    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", banhxeo_data)
    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", comtam_data)
    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", goicuon_data)

    conn.commit()
    conn.close()

def get_dish_data(dish_name):
    conn = sqlite3.connect('calorie_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM dishes WHERE name=?", (dish_name,))
    result = c.fetchone()
    conn.close()
    return result

if __name__ == "__main__":
    create_database()
