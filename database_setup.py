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
        ('Banh mi', 'Baguette', 120, 310, 'High in carbs'),
        ('Banh mi', 'Pork', 60, 170, 'Grilled or steamed'),
        ('Banh mi', 'Pickled veggies', 30, 15, 'Carrot, daikon'),
        ('Banh mi', 'Cucumber', 20, 5, ''),
        ('Banh mi', 'Cilantro & chili', 5, 2, ''),
        ('Banh mi', 'Mayonnaise', 15, 100, '')
    ]

    banhxeo_data = [
        ('Banh xeo', 'Rice flour batter', 150, 260, 'Made with coconut milk'),
        ('Banh xeo', 'Pork', 50, 140, 'Sliced'),
        ('Banh xeo', 'Shrimp', 40, 50, 'Medium-sized'),
        ('Banh xeo', 'Mung beans', 30, 90, 'Steamed'),
        ('Banh xeo', 'Bean sprouts', 50, 10, 'Low cal'),
        ('Banh xeo', 'Herbs & lettuce', 20, 5, 'Basil, mint, lettuce')
    ]

    comtam_data = [
        ('Com tam', 'Broken rice', 200, 260, 'High in carbs'),
        ('Com tam', 'Grilled pork chop', 120, 340, 'Marinated'),
        ('Com tam', 'Shredded pork skin', 50, 100, 'With toasted rice powder'),
        ('Com tam', 'Steamed egg meatloaf', 80, 170, 'Egg, ground pork, glass noodles'),
        ('Com tam', 'Pickled veggies', 30, 15, ''),
        ('Com tam', 'Fish sauce dip', 30, 45, 'Sweet-savory')
    ]

    goicuon_data = [
        ('Goi cuon', 'Rice paper', 20, 35, 'Thin wrapper'),
        ('Goi cuon', 'Shrimp', 50, 60, 'Boiled'),
        ('Goi cuon', 'Pork belly', 50, 180, 'Boiled and sliced'),
        ('Goi cuon', 'Vermicelli noodles', 60, 90, 'Soft rice noodles'),
        ('Goi cuon', 'Herbs & lettuce', 30, 6, 'Mint, basil, lettuce'),
        ('Goi cuon', 'Peanut hoisin sauce', 30, 100, 'Sweet-savory')
    ]

    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", pho_data)
    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", banhmi_data)
    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", banhxeo_data)
    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", comtam_data)
    c.executemany("INSERT INTO dish_info VALUES (?, ?, ?, ?, ?)", goicuon_data)

    conn.commit()
    conn.close()

def get_total_calories(dish_name):
    """Return total calories for a given dish."""
    conn = sqlite3.connect('calories.db')
    c = conn.cursor()

    c.execute("SELECT SUM(calories) FROM dish_info WHERE dish_name = ?", (dish_name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result and result[0] is not None else 0

def get_full_dish_data(dish_name):
    """Return full rows for a given dish."""
    conn = sqlite3.connect('calories.db')
    c = conn.cursor()

    c.execute("SELECT * FROM dish_info WHERE dish_name = ?", (dish_name,))
    result = c.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    create_database()
