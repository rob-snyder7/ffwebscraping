
# https://fantasyfootballcalculator.com/rankings/ppr/defense
# pulled PPR on 5/7/2018

FCal = ['Ezekiel Elliott', 'Todd Gurley', 'LeVeon Bell', 'Antonio Brown', 'David Johnson', 'Alvin Kamara', 'DeAndre Hopkins', 'Saquon Barkley', 'Leonard Fournette', 'Odell Beckham Jr', 'Melvin Gordon', 'Kareem Hunt', 'Dalvin Cook', 'Julio Jones', 'Michael Thomas', 'Christian McCaffrey', 'Davante Adams', 'Devonta Freeman', 'LeSean McCoy', 'Keenan Allen', 'A.J. Green', 'Mark Ingram', 'Mike Evans', 'Jordan Howard', 'Jerick McKinnon', 'Rob Gronkowski', 'Joe Mixon', 'Tyreek Hill', 'Derrick Henry', 'Adam Thielen', 'Aaron Rodgers', 'Travis Kelce', 'Doug Baldwin', 'Deshaun Watson', 'T.Y. Hilton', 'Zach Ertz', 'Jay Ajayi', 'Stefon Diggs', 'Amari Cooper', 'Josh Gordon', 'Kenyan Drake', 'Larry Fitzgerald', 'Allen Robinson', 'Alex Collins', 'Alshon Jeffery', 'Demaryius Thomas', 'Brandin Cooks', 'Jarvis Landry', 'Lamar Miller', 'Jimmy Graham', 'Russell Wilson', 'Carlos Hyde', 'Golden Tate', 'Carson Wentz', 'JuJu Smith-Schuster', 'Tom Brady', 'Dion Lewis', 'Michael Crabtree', 'Julian Edelman', 'Derrius Guice', 'Greg Olsen', 'Rex Burkhead', 'Tevin Coleman', 'Evan Engram', 'Devin Funchess', 'Hunter Henry', 'Tarik Cohen', 'Corey Davis', 'Chris Hogan', 'Pierre Garcon', 'Cam Newton', 'Drew Brees', 'Marvin Jones', 'Chris Thompson', 'Jordy Nelson', 'Ty Montgomery', 'Duke Johnson', 'Kyle Rudolph', 'Sammy Watkins', 'Sony Michel', 'Will Fuller', 'Jimmy Garoppolo', 'Marshawn Lynch', 'Kirk Cousins', 'Delanie Walker', 'Jamaal Williams', 'Robert Woods', 'Chris Carson', 'Emmanuel Sanders', 'Robby Anderson', 'Jared Goff', 'Rashaad Penny', 'Cooper Kupp', 'Marlon Mack', 'Aaron Jones', 'Jacksonville', 'Jamison Crowder', 'Isaiah Crowell', 'Jordan Reed', 'DeVante Parker', 'Devontae Booker', 'Marquise Goodwin', 'Trey Burton', 'Matthew Stafford', 'Kelvin Benjamin', 'Ronald Jones', 'Randall Cobb', 'LeGarrette Blount', 'LA Rams', 'Ben Roethlisberger', 'Nick Chubb', 'Philip Rivers', 'Donta Foreman', 'Cameron Meredith', 'Andrew Luck', 'Theo Riddick', 'Nelson Agholor', 'Minnesota', 'Matt Ryan', 'Tyler Eifert', 'James White', 'Sterling Shepard', 'Derek Carr', 'Martavis Bryant', 'Houston', 'Dak Prescott', 'Marqise Lee', 'Philadelphia', 'Calvin Ridley', 'Pat Mahomes', 'Samaje Perine', 'Josh Doctson', 'LA Chargers', 'Allen Hurns', 'Baltimore', 'George Kittle', 'Marcus Mariota', 'Royce Freeman', 'Kerryon Johnson', 'Giovani Bernard', 'Courtland Sutton', 'Greg Zuerlein', 'Mohamed Sanu', 'Jameis Winston', 'Jack Doyle', 'Denver', 'Danny Amendola', 'Corey Clement', 'DJ Moore', 'Latavius Murray', 'Jeremy Hill', 'Justin Tucker', 'Alex Smith', 'Stephen Gostkowski', 'O.J. Howard', 'Case Keenum', 'Dede Westbrook', 'Rishard Matthews', 'Peyton Barber', 'DeSean Jackson', 'Spencer Ware', 'Carolina', 'David Njoku', 'Bilal Powell', 'Kenny Golladay', 'Doug Martin', 'Mike Williams', 'Terrelle Pryor', 'Tyrod Taylor', 'New Orleans', 'Eric Ebron', 'Jordan Matthews', 'Mitch Trubisky', 'Kansas City', 'Wil Lutz', 'Austin Seferian-Jenkins', 'Paul Richardson', 'Pittsburgh', 'Lamar Jackson', 'Jake Elliott', 'Robbie Gould', 'Matt Bryant', 'Harrison Butker', 'Chris Boswell', 'Hayden Hurst', 'Kenny Stills', 'New England', 'Matt Prater', 'Dan Bailey', 'Mason Crosby', 'Frank Gore', 'Eli Manning', 'Cameron Brate', 'Graham Gano', 'Seattle', 'Blake Bortles', 'Mike Gesicki', 'Ted Ginn Jr', 'Ryan Succop', 'Baker Mayfield']

FCqb = ['Aaron Rodgers', 'Deshaun Watson', 'Russell Wilson', 'Carson Wentz', 'Tom Brady', 'Cam Newton', 'Drew Brees', 'Jimmy Garoppolo', 'Kirk Cousins', 'Jared Goff', 'Matthew Stafford', 'Ben Roethlisberger', 'Philip Rivers', 'Andrew Luck', 'Matt Ryan', 'Derek Carr', 'Dak Prescott', 'Pat Mahomes', 'Marcus Mariota', 'Jameis Winston', 'Alex Smith', 'Case Keenum', 'Tyrod Taylor', 'Mitch Trubisky', 'Lamar Jackson', 'Eli Manning', 'Blake Bortles', 'Baker Mayfield', 'Nick Foles', 'Sam Darnold', 'Joe Flacco', 'Josh Allen']

FCrb = ['Ezekiel Elliott', 'Todd Gurley', 'LeVeon Bell', 'David Johnson', 'Alvin Kamara', 'Saquon Barkley', 'Leonard Fournette', 'Melvin Gordon', 'Kareem Hunt', 'Dalvin Cook', 'Christian McCaffrey', 'Devonta Freeman', 'LeSean McCoy', 'Mark Ingram', 'Jordan Howard', 'Jerick McKinnon', 'Joe Mixon', 'Derrick Henry', 'Jay Ajayi', 'Kenyan Drake', 'Alex Collins', 'Lamar Miller', 'Carlos Hyde', 'Dion Lewis', 'Derrius Guice', 'Rex Burkhead', 'Tevin Coleman', 'Tarik Cohen', 'Chris Thompson', 'Ty Montgomery', 'Duke Johnson', 'Sony Michel', 'Marshawn Lynch', 'Jamaal Williams', 'Chris Carson', 'Rashaad Penny', 'Marlon Mack', 'Aaron Jones', 'Isaiah Crowell', 'Devontae Booker', 'Ronald Jones', 'LeGarrette Blount', 'Nick Chubb', 'Donta Foreman', 'Theo Riddick', 'James White', 'Samaje Perine', 'Royce Freeman', 'Kerryon Johnson', 'Giovani Bernard', 'Corey Clement', 'Latavius Murray', 'Jeremy Hill', 'Peyton Barber', 'Spencer Ware', 'Bilal Powell', 'Doug Martin', 'Frank Gore', 'Akeem Hunt', 'Ameer Abdullah', 'Chris Thompson', 'James Conner', 'Jonathan Stewart', 'Akrum Wadley', 'Matt Breida', 'Rob Kelley', 'Michael Bush', 'DeDe Dorsey', 'Matt Forte', 'Kevin Smith', 'Jacob Hester', 'Ryan Torain', 'Andre Hall', 'Tim Castille', 'Zak Keasey', 'Korey Hall', 'Mike Cox', 'Owen Schmitt', 'Kregg Lumpkin', 'Gary Russell']

FCwr = ['Antonio Brown', 'DeAndre Hopkins', 'Odell Beckham Jr', 'Julio Jones', 'Michael Thomas', 'Davante Adams', 'Keenan Allen', 'A.J. Green', 'Mike Evans', 'Tyreek Hill', 'Adam Thielen', 'Doug Baldwin', 'T.Y. Hilton', 'Stefon Diggs', 'Amari Cooper', 'Josh Gordon', 'Larry Fitzgerald', 'Allen Robinson', 'Alshon Jeffery', 'Demaryius Thomas', 'Brandin Cooks', 'Jarvis Landry', 'Golden Tate', 'JuJu Smith-Schuster', 'Michael Crabtree', 'Julian Edelman', 'Devin Funchess', 'Corey Davis', 'Chris Hogan', 'Pierre Garcon', 'Marvin Jones', 'Jordy Nelson', 'Sammy Watkins', 'Will Fuller', 'Robert Woods', 'Emmanuel Sanders', 'Robby Anderson', 'Cooper Kupp', 'Jamison Crowder', 'DeVante Parker', 'Marquise Goodwin', 'Kelvin Benjamin', 'Randall Cobb', 'Cameron Meredith', 'Nelson Agholor', 'Sterling Shepard', 'Martavis Bryant', 'Marqise Lee', 'Calvin Ridley', 'Josh Doctson', 'Allen Hurns', 'Courtland Sutton', 'Mohamed Sanu', 'Danny Amendola', 'DJ Moore', 'Dede Westbrook', 'Rishard Matthews', 'DeSean Jackson', 'Kenny Golladay', 'Mike Williams', 'Terrelle Pryor', 'Jordan Matthews', 'Paul Richardson', 'Kenny Stills', 'Ted Ginn Jr', 'Tavon Austin', 'Michael Gallup', 'Donte Moncrief', 'Zay Jones', 'Tyler Lockett', 'Tommylee Lewis', 'John Brown', 'Ryan Grant', 'Anthony Miller', 'Christian Kirk', 'Curtis Samuel', 'Devin Aromashodu', 'Steve Breaston', 'Nate Burleson', 'Terrance Copper']

FCte = ['Rob Gronkowski', 'Travis Kelce', 'Zach Ertz', 'Jimmy Graham', 'Greg Olsen', 'Evan Engram', 'Hunter Henry', 'Kyle Rudolph', 'Delanie Walker', 'Jordan Reed', 'Trey Burton', 'Tyler Eifert', 'George Kittle', 'Jack Doyle', 'O.J. Howard', 'David Njoku', 'Eric Ebron', 'Austin Seferian-Jenkins', 'Hayden Hurst', 'Cameron Brate', 'Mike Gesicki', 'Jason Witten', 'Kevin Boss', 'Jesse James', 'Vernon Davis', 'Clark Harris', 'Benjamin Watson', 'Brad Cottam', 'Jermichael Finley', 'Martin Rucker', 'Derek Fine', 'Tom Santi']


# https://www.fantasypros.com/nfl/rankings/ppr-cheatsheets.php
# pulled PPR on 5/7/2018

FPal = ["LeVeon Bell", 'Todd Gurley', 'Antonio Brown', 'David Johnson', 'DeAndre Hopkins', 'Odell Beckham Jr.', 'Ezekiel Elliott', 'Alvin Kamara', 'Michael Thomas', 'Julio Jones', 'Keenan Allen', 'Kareem Hunt', 'A.J. Green', 'Davante Adams', 'Mike Evans', 'Melvin Gordon', 'Leonard Fournette', 'Adam Thielen', 'Dalvin Cook', 'Tyreek Hill', 'Doug Baldwin', 'Saquon Barkley', 'Christian McCaffrey', 'Rob Gronkowski', 'Devonta Freeman', 'T.Y. Hilton', 'Josh Gordon', 'Travis Kelce', 'Stefon Diggs', 'Larry Fitzgerald', 'LeSean McCoy', 'Mark Ingram', 'Alshon Jeffery', 'Jerick McKinnon', 'Zach Ertz', 'Aaron Rodgers', 'Demaryius Thomas', 'Amari Cooper', 'Golden Tate', 'Allen Robinson', 'Kenyan Drake', 'Jarvis Landry', 'Jordan Howard', 'Joe Mixon', 'Russell Wilson', 'Brandin Cooks', 'Tom Brady', 'JuJu Smith-Schuster', 'Alex Collins', 'Derrick Henry', 'Deshaun Watson', 'Evan Engram', 'Michael Crabtree', 'Robert Woods', 'Jay Ajayi', 'Carson Wentz', 'Cam Newton', 'Marvin Jones', 'Dion Lewis', 'Dez Bryant', 'Greg Olsen', 'Drew Brees', 'Hunter Henry', 'Pierre Garcon', 'Chris Thompson', 'Sammy Watkins', 'Duke Johnson', 'Devin Funchess', 'Marlon Mack', 'Kirk Cousins', 'Lamar Miller', 'Corey Davis', 'Tevin Coleman', 'Jimmy Graham', 'Jamison Crowder', 'Cooper Kupp', 'Delanie Walker', 'Matthew Stafford', 'Kyle Rudolph', 'Emmanuel Sanders', 'Jordy Nelson', 'Sterling Shepard', 'Chris Hogan', 'Rex Burkhead', 'Devante Parker', 'Will Fuller', 'Derrius Guice', 'Jimmy Garoppolo', 'Robby Anderson', 'Marqise Lee', 'Andrew Luck', 'Carlos Hyde', 'Nelson Agholor', 'Rashaad Penny', 'Ben Roethlisberger', 'Jared Goff', 'Marshawn Lynch', 'Marquise Goodwin', 'Aaron Jones', 'Jack Doyle', 'Kelvin Benjamin', 'Theo Riddick', 'Julian Edelman', 'Philip Rivers', 'Randall Cobb', 'Tarik Cohen', 'Jamaal Williams', 'Bilal Powell', 'Isaiah Crowell', 'Dak Prescott', 'Sony Michel', 'Jordan Reed', 'Matt Ryan', 'Josh Doctson', 'James White', 'Jameis Winston', 'DeSean Jackson', 'Trey Burton', 'Ronald Jones II', 'Royce Freeman', 'Marcus Mariota', 'Rishard Matthews', "D'Onta Foreman", 'Tyler Eifert', 'C.J. Anderson', 'Patrick Mahomes', 'Martavis Bryant', 'O.J. Howard', 'Mohamed Sanu', 'George Kittle', 'David Njoku', 'Eric Ebron', 'Nick Chubb', 'Dede Westbrook', 'Alex Smith', 'Ted Ginn', 'Jacksonville Jaguars', 'Chris Carson', 'Cameron Brate', 'Ty Montgomery', 'Charles Clay', 'Devontae Booker', 'Minnesota Vikings', 'Derek Carr', 'Kenny Stills', 'Samaje Perine', 'Corey Coleman', 'Wayne Gallman', 'Giovani Bernard', 'Philadelphia Eagles', 'Donte Moncrief', 'DeMarco Murray', 'Allen Hurns', 'Mike Wallace', 'Doug Martin', 'Blake Bortles', 'Jared Cook', 'Frank Gore', 'Denver Broncos', 'Latavius Murray', 'Los Angeles Rams', 'Austin Seferian-Jenkins', 'Kerryon Johnson', 'Mike Williams', 'LeGarrette Blount', 'Kenny Golladay', 'Paul Richardson', 'Tyler Lockett', 'Peyton Barber', 'Mitch Trubisky', 'Calvin Ridley', 'Ameer Abdullah', 'Andy Dalton', 'Los Angeles Chargers', 'Houston Texans', 'Case Keenum', 'Austin Hooper', 'Matt Breida', 'Seattle Seahawks', 'Stephen Gostkowski', 'Corey Clement', 'Baltimore Ravens', 'Jordan Matthews', 'Justin Tucker', 'Tyrod Taylor', 'Eli Manning', 'Chris Godwin', 'Cameron Meredith', 'Jonathan Stewart', 'Vance McDonald', 'D.J. Moore', 'Danny Amendola', 'Terrelle Pryor', 'Greg Zuerlein', 'Tyrell Williams', 'Jeremy Maclin', 'Benjamin Watson', 'T.J. Yeldon', 'Matt Bryant', 'Austin Ekeler', 'John Brown', 'Albert Wilson', 'Cole Beasley', 'Kenneth Dixon', 'Willie Snead', 'Jermaine Kearse', 'Adam Shaheen', 'Terrance Williams', 'Mike Gesicki', 'Darren Sproles', 'Kansas City Chiefs', 'Dan Bailey', 'Anthony Miller', 'Zay Jones', 'Spencer Ware', 'New England Patriots', 'Christian Kirk', 'Ryan Tannehill', 'New Orleans Saints', 'Wil Lutz', 'Michael Gallup', 'Matt Prater', 'Geronimo Allison', 'James Washington', 'Keelan Cole', 'Joe Flacco', 'Carolina Panthers', 'Josh Hill', 'Orleans Darkwa', 'Eric Decker', 'Vernon Davis', 'Joe Williams', 'Pittsburgh Steelers', 'Ryan Grant', 'Tyler Kroft', 'Kenny Britt', 'Quincy Enunwa', 'Javorius Allen', 'Mike Davis', 'Courtland Sutton', 'Lamar Jackson', 'Brandon LaFell', 'Kendall Wright', 'Arizona Cardinals', 'Hayden Hurst', 'Ricky Seals-Jones', 'Terrance West', 'Gerald Everett', 'Cameron Artis-Payne', 'Nyheim Hines', 'Mason Crosby', 'Rod Smith', 'Rico Gathers', 'Chicago Bears', 'C.J. Fiedorowicz', 'Chris Boswell', 'Mike Gillislee', 'Jeremy Hill', 'Malcolm Mitchell', 'Brice Butler', 'Atlanta Falcons', 'Stephen Anderson', 'Jake Elliott', 'Curtis Samuel', 'Paul Perkins', 'C.J. Prosise', 'Jesse James', 'J.J. Nelson', 'Robert Turbin', 'Harrison Butker', 'Coby Fleener', 'Chris Ivory', 'Shane Vereen', 'Jalen Richard', 'Adam Vinatieri', 'Josh Reynolds', 'DeAndre Washington', 'Torrey Smith', 'Jake Butt', 'Eddie Lacy', 'John Ross', 'Jamaal Charles', 'Josh McCown', 'Brandon Marshall', 'Kevin White', 'New York Giants', 'Jacquizz Rodgers', 'Corey Grant', 'Ryan Griffin', 'Brandon McManus', 'Charles Sims', 'Graham Gano', "De'Angelo Henderson", 'Jaron Brown', 'Travis Benjamin', 'Buffalo Bills', 'Sam Bradford', 'Dallas Goedert', 'Blair Walsh', 'Tampa Bay Buccaneers', 'Adrian Peterson', 'Elijah McGuire', 'Thomas Rawls', 'Green Bay Packers', 'Cincinnati Bengals', 'Josh Allen', 'Tennessee Titans', 'Teddy Bridgewater', 'Nick Vannett', 'Cairo Santos', 'Robbie Gould', 'Kai Forbath', 'Mark Andrews', 'Taylor Gabriel', 'Garrett Celek', 'Amara Darboh', 'Carlos Henderson', 'Adam Humphries', 'Deon Cain', 'DaeSean Hamilton', 'Elijhaa Penny', 'Ed Dickson', 'Trent Taylor', 'Dontrelle Inman', 'Steven Hauschka', 'Breshad Perriman', 'Phil Dawson', 'Chase Edmonds', 'Luke Willson', 'Tyler Higbee', 'Taywan Taylor', 'Baker Mayfield', 'Chester Rogers', 'Andre Holmes', 'Ryan Succop', 'AJ McCarron', 'Sam Darnold', 'Kyle Juszczyk', 'Josh Rosen', 'James Conner', 'Braxton Miller', 'Jermaine Gresham', 'San Francisco 49ers', 'Jonnu Smith', 'Maxx Williams', 'Antonio Gates', 'Demarcus Robinson', 'Chris Conley', 'Caleb Sturgis', 'Mike Tolbert', 'Wendell Smallwood', 'Michael Roberts', 'Dante Pettis', 'Detroit Lions', 'Clive Walford', 'ArDarius Stewart', 'D.J. Chark', 'Kalen Ballage', 'Pharoh Cooper', 'Tion Green', "J'Mon Moore", 'Jeff Heuerman', 'Oakland Raiders', 'Roger Lewis', 'Malcolm Brown', 'Tavon Austin', 'Nick Foles', 'Demetrius Harris', 'Cleveland Browns', "Ka'imi Fairbairn", 'Damien Williams', 'Charcandrick West', 'Alfred Blue', 'Josh Lambo', 'Jordan Akins', 'Laquon Treadwell', 'New York Jets', 'Antonio Callaway', "Tre'Quan Smith", 'Tyler Boyd', 'Kerwynn Williams', 'Miami Dolphins', 'Chad Williams', 'Washington Redskins', 'Mack Hollins']

FPqb = ['Aaron Rodgers', 'Russell Wilson', 'Tom Brady', 'Deshaun Watson', 'Carson Wentz', 'Cam Newton', 'Drew Brees', 'Kirk Cousins', 'Matthew Stafford', 'Jimmy Garoppolo', 'Ben Roethlisberger', 'Andrew Luck', 'Jared Goff', 'Philip Rivers', 'Dak Prescott', 'Matt Ryan', 'Jameis Winston', 'Marcus Mariota', 'Patrick Mahomes', 'Alex Smith', 'Derek Carr', 'Blake Bortles', 'Mitch Trubisky', 'Andy Dalton', 'Tyrod Taylor', 'Case Keenum', 'Eli Manning', 'Joe Flacco', 'Ryan Tannehill', 'Josh McCown', 'Sam Bradford', 'Josh Allen', 'Teddy Bridgewater', 'Lamar Jackson', 'Baker Mayfield', 'AJ McCarron', 'Sam Darnold', 'Josh Rosen', 'Nick Foles', 'Jacoby Brissett', 'Mason Rudolph', 'Kyle Lauletta', 'DeShone Kizer', 'Trevor Siemian', 'Drew Stanton', 'Paxton Lynch', 'Jay Cutler', 'Ryan Fitzpatrick', 'Cody Kessler', 'Mike Glennon', 'Brian Hoyer', 'Brock Osweiler', 'Colin Kaepernick', 'Chad Henne']

FPrb = ["LeVeon Bell", 'Todd Gurley', 'David Johnson', 'Ezekiel Elliott', 'Alvin Kamara', 'Kareem Hunt', 'Melvin Gordon', 'Leonard Fournette', 'Dalvin Cook', 'Saquon Barkley', 'Christian McCaffrey', 'Devonta Freeman', 'LeSean McCoy', 'Mark Ingram', 'Jerick McKinnon', 'Kenyan Drake', 'Jordan Howard', 'Joe Mixon', 'Alex Collins', 'Derrick Henry', 'Dion Lewis', 'Jay Ajayi', 'Chris Thompson', 'Duke Johnson', 'Lamar Miller', 'Marlon Mack', 'Tevin Coleman', 'Derrius Guice', 'Rex Burkhead', 'Carlos Hyde', 'Rashaad Penny', 'Aaron Jones', 'Marshawn Lynch', 'Theo Riddick', 'Jamaal Williams', 'Sony Michel', 'Bilal Powell', 'Ronald Jones II', 'Tarik Cohen', 'Isaiah Crowell', 'Royce Freeman', 'James White', 'C.J. Anderson', "D'Onta Foreman", 'Nick Chubb', 'Chris Carson', 'Ty Montgomery', 'Samaje Perine', 'Devontae Booker', 'Kerryon Johnson', 'DeMarco Murray', 'Wayne Gallman', 'Ameer Abdullah', 'Frank Gore', 'Peyton Barber', 'Giovani Bernard', 'Doug Martin', 'Matt Breida', 'Latavius Murray', 'Corey Clement', 'LeGarrette Blount', 'Kenneth Dixon', 'Jonathan Stewart', 'Joe Williams', 'T.J. Yeldon', 'Austin Ekeler', 'Orleans Darkwa', 'Darren Sproles', 'Mike Davis', 'Jeremy Hill', 'Terrance West', 'Nyheim Hines', 'Paul Perkins', 'Spencer Ware', 'Rod Smith', 'Shane Vereen', 'Javorius Allen', 'Robert Turbin', 'C.J. Prosise', 'Cameron Artis-Payne', 'DeAndre Washington', 'Mike Gillislee', 'Jalen Richard', 'Charles Sims', 'Chris Ivory', 'Adrian Peterson', 'James Conner', "De'Angelo Henderson", 'Kyle Juszczyk', 'Jacquizz Rodgers', 'Elijah McGuire', 'Thomas Rawls', 'Kalen Ballage', 'Elijhaa Penny', 'Jordan Wilkins', 'Eddie Lacy', 'Damien Williams', 'Corey Grant', 'John Kelly', 'Tion Green', 'Charcandrick West', 'Mark Walton', 'Alfred Blue', 'Malcolm Brown', 'Wendell Smallwood', 'Chase Edmonds', 'Jamaal Charles', 'Fozzy Whittaker', 'Jonathan Williams', 'Travaris Cadet', 'Justin Jackson', 'Kerwynn Williams', 'Christine Michael', 'Bo Scarbrough', 'J.D. McKissic', 'Branden Oliver', 'Josh Adams', 'Ito Smith', 'Robert Kelley', 'Mike Tolbert', 'Dwayne Washington', 'Alfred Morris', 'Zach Zenner', 'Elijah Hood', 'Marcus Murphy', 'Jeremy McNichols', 'Matt Jones', 'Jeremy Langford']

FPwr = ['Antonio Brown', 'DeAndre Hopkins', 'Odell Beckham Jr.', 'Michael Thomas', 'Julio Jones', 'Keenan Allen', 'A.J. Green', 'Davante Adams', 'Mike Evans', 'Adam Thielen', 'Doug Baldwin', 'Tyreek Hill', 'T.Y. Hilton', 'Josh Gordon', 'Stefon Diggs', 'Larry Fitzgerald', 'Alshon Jeffery', 'Demaryius Thomas', 'Amari Cooper', 'Allen Robinson', 'Golden Tate', 'Jarvis Landry', 'Brandin Cooks', 'JuJu Smith-Schuster', 'Michael Crabtree', 'Robert Woods', 'Marvin Jones', 'Dez Bryant', 'Pierre Garcon', 'Sammy Watkins', 'Devin Funchess', 'Corey Davis', 'Jamison Crowder', 'Cooper Kupp', 'Emmanuel Sanders', 'Jordy Nelson', 'Sterling Shepard', 'Chris Hogan', 'Devante Parker', 'Will Fuller', 'Robby Anderson', 'Marqise Lee', 'Nelson Agholor', 'Julian Edelman', 'Marquise Goodwin', 'Kelvin Benjamin', 'Randall Cobb', 'Josh Doctson', 'DeSean Jackson', 'Rishard Matthews', 'Dede Westbrook', 'Martavis Bryant', 'Mohamed Sanu', 'Kenny Stills', 'Ted Ginn', 'Corey Coleman', 'Allen Hurns', 'Donte Moncrief', 'Kenny Golladay', 'Calvin Ridley', 'Mike Williams', 'Paul Richardson', 'Mike Wallace', 'Tyler Lockett', 'Jordan Matthews', 'D.J. Moore', 'Jeremy Maclin', 'Chris Godwin', 'Terrelle Pryor', 'Cameron Meredith', 'Danny Amendola', 'Terrance Williams', 'James Washington', 'Tyrell Williams', 'John Brown', 'Geronimo Allison', 'Jermaine Kearse', 'Keelan Cole', 'Ryan Grant', 'Albert Wilson', 'Malcolm Mitchell', 'Quincy Enunwa', 'Brice Butler', 'Zay Jones', 'Cole Beasley', 'Christian Kirk', 'Michael Gallup', 'Willie Snead', 'Courtland Sutton', 'Eric Decker', 'Anthony Miller', 'Kendall Wright', 'Torrey Smith', 'Taylor Gabriel', 'Curtis Samuel', 'John Ross', 'Kevin White', 'Trent Taylor', 'Brandon LaFell', 'Kenny Britt', 'Travis Benjamin', 'J.J. Nelson', 'Jaron Brown', 'Taywan Taylor', 'Demarcus Robinson', 'Chris Conley', 'Josh Reynolds', 'Adam Humphries', 'Dante Pettis', 'Carlos Henderson', 'ArDarius Stewart', 'Dontrelle Inman', 'Brandon Marshall', 'Brandon Coleman', 'Cordarrelle Patterson', 'Chester Rogers', 'Andre Holmes', 'Bruce Ellington', 'Tavon Austin', 'Braxton Miller', 'Tyler Boyd', 'Breshad Perriman', 'Laquon Treadwell', 'Jakeem Grant', 'Chad Williams', 'Mack Hollins', 'Amara Darboh', 'Phillip Dorsett', 'Auden Tate', 'Seth Roberts', 'Aldrick Robinson', 'Pharoh Cooper', 'Roger Lewis', 'Equanimeous St. Brown', 'Antonio Callaway', 'Marcell Ateman', 'D.J. Chark', 'Kasen Williams', 'Deon Cain', "Tre'Quan Smith", 'Cody Latimer', 'Simmie Cobbs Jr.', 'Marcus Johnson', 'Chris Moore', 'Ryan Switzer', 'Damiere Byrd', 'Rod Streater', 'DaeSean Hamilton', 'Keke Coutee', 'Leonte Carroo', 'Chris Thompson', "J'Mon Moore", 'Deonte Thompson', 'TJ Jones', 'Ricardo Louis', 'Michael Floyd', 'Eli Rogers', 'Sammie Coates', 'Jordan Lasley', 'Jaydon Mickens', 'Jaleel Scott']

FPte = ['Rob Gronkowski', 'Travis Kelce', 'Zach Ertz', 'Evan Engram', 'Greg Olsen', 'Hunter Henry', 'Jimmy Graham', 'Delanie Walker', 'Kyle Rudolph', 'Jack Doyle', 'Trey Burton', 'Jordan Reed', 'Tyler Eifert', 'O.J. Howard', 'George Kittle', 'David Njoku', 'Eric Ebron', 'Charles Clay', 'Cameron Brate', 'Austin Seferian-Jenkins', 'Jared Cook', 'Austin Hooper', 'Vance McDonald', 'Mike Gesicki', 'Benjamin Watson', 'Adam Shaheen', 'Tyler Kroft', 'Josh Hill', 'Hayden Hurst', 'Gerald Everett', 'Vernon Davis', 'Rico Gathers', 'Coby Fleener', 'Jake Butt', 'Stephen Anderson', 'Ricky Seals-Jones', 'Nick Vannett', 'Jesse James', 'C.J. Fiedorowicz', 'Ryan Griffin', 'Garrett Celek', 'Luke Willson', 'Jaylen Samuels', 'Ed Dickson', 'Tyler Higbee', 'Jonnu Smith', 'Jermaine Gresham', 'Mark Andrews', 'Dallas Goedert', 'Antonio Gates', 'Clive Walford', 'Lance Kendricks', 'Michael Roberts', 'Dion Sims', 'Seth DeValve', 'Dwayne Allen', 'Demetrius Harris', 'Ian Thomas', 'Maxx Williams', "Nick O'Leary", 'Julius Thomas', 'Niles Paul', 'Virgil Green', 'Jordan Akins', 'Nick Boyle', 'Jordan Leggett', 'A.J. Derby', 'Eric Tomlinson', 'Jeff Heuerman', 'Troy Niklas', 'Marcedes Lewis', 'Troy Fumagalli']


# http://www.espn.com/fantasy/football/story/_/id/23403473/fantasy-football-summit-point-per-reception-rankings-2018-overall-position
# pulled PPR on 5/7/2018

ESal = ['LeVeon Bell', 'Todd Gurley', 'David Johnson', 'Antonio Brown', 'Ezekiel Elliott', 'DeAndre Hopkins', 'Odell Beckham Jr', 'Kareem Hunt', 'Alvin Kamara', 'Saquon Barkley', 'Julio Jones', 'Michael Thomas', 'Keenan Allen', 'Leonard Fournette', 'AJ Green', 'Davante Adams', 'Melvin Gordon', 'Dalvin Cook', 'Mike Evans', 'LeSean McCoy', 'Christian McCaffrey', 'Devonta Freeman', 'Rob Gronkowski', 'Travis Kelce', 'Adam Thielen', 'Aaron Rodgers', 'Doug Baldwin', 'Tyreek Hill', 'Tom Brady', 'Mark Ingram', 'Jerick McKinnon', 'Larry Fitzgerald', 'TY Hilton', 'Joe Mixon', 'Zach Ertz', 'Demaryius Thomas', 'Stefon Diggs', 'Allen Robinson', 'Alshon Jeffery', 'Russell Wilson', 'Jordan Howard', 'Kenyan Drake', 'Golden Tate', 'Josh Gordon', 'Jay Ajayi', 'Derrick Henry', 'Derrius Guice', 'Jarvis Landry', 'Julian Edelman', 'Alex Collins']

ESqb = ['Aaron Rodgers', 'Tom Brady', 'Russell Wilson', 'Deshaun Watson', 'Cam Newton', 'Carson Wentz', 'Drew Brees', 'Kirk Cousins', 'Andrew Luck', 'Jimmy Garoppolo', 'Matthew Stafford', 'Ben Roethlisberger', 'Philip Rivers', 'Dak Prescott', 'Alex Smith', 'Patrick Mahomes', 'Jared Goff', 'Matt Ryan', 'Jameis Winston', 'Marcus Mariota', 'Derek Carr', 'Tyrod Taylor', 'Mitchell Trubisky', 'Blake Bortles', 'Case Keenum', 'Andy Dalton', 'Eli Manning', 'Ryan Tannehill', 'Sam Bradford', 'Josh McCown']

ESrb = ["Le'Veon Bell", 'Todd Gurley', 'David Johnson', 'Ezekiel Elliott', 'Kareem Hunt', 'Alvin Kamara', 'Saquon Barkley', 'Leonard Fournette', 'Melvin Gordon', 'Dalvin Cook', 'LeSean McCoy', 'Christian McCaffrey', 'Devonta Freeman', 'Mark Ingram', 'Jerick McKinnon', 'Joe Mixon', 'Jordan Howard', 'Kenyan Drake', 'Jay Ajayi', 'Derrick Henry', 'Derrius Guice', 'Alex Collins', 'Lamar Miller', 'Rashaad Penny', 'Dion Lewis', 'Marshawn Lynch', 'Sony Michel', 'Duke Johnson Jr', 'Chris Thompson', 'Royce Freeman', 'Rex Burkhead', 'Tevin Coleman', 'Tarik Cohen', 'Carlos Hyde', 'Ronald Jones II', 'Nick Chubb', 'Jamaal Williams', 'Marlon Mack', 'Isaiah Crowell', 'Aaron Jones', 'James White', 'Theo Riddick', 'Bilal Powell', 'LeGarrette Blount', 'Kerryon Johnson', 'Devontae Booker', "D'Onta Foreman", 'Giovani Bernard', 'Ty Montgomery', 'Chris Carson', 'Corey Clement', 'Latavius Murray', 'Jonathan Stewart', 'Peyton Barber', 'Frank Gore', 'Kenneth Dixon', 'Matt Breida', 'Doug Martin', 'Rob Kelley']

ESwr = ['Antonio Brown', 'DeAndre Hopkins', 'Odell Beckham Jr', 'Julio Jones', 'Michael Thomas', 'Keenan Allen', 'A.J. Green', 'Davante Adams', 'Mike Evans', 'Adam Thielen', 'Doug Baldwin', 'Tyreek Hill', 'Larry Fitzgerald', 'T.Y. Hilton', 'Demaryius Thomas', 'Stefon Diggs', 'Allen Robinson', 'Alshon Jeffery', 'Golden Tate', 'Josh Gordon', 'Jarvis Landry', 'Julian Edelman', 'Amari Cooper', 'JuJu Smith-Schuster', 'Michael Crabtree', 'Robert Woods', 'Brandin Cooks', 'Devin Funchess', 'Marvin Jones Jr', 'Emmanuel Sanders', 'Chris Hogan', 'Pierre Garcon', 'Cooper Kupp', 'Corey Davis', 'Will Fuller V', 'Robby Anderson', 'Sammy Watkins', 'Jamison Crowder', 'Randall Cobb', 'Kelvin Benjamin', 'Jordy Nelson', 'Marquise Goodwin', 'DeVante Parker', 'Marqise Lee', 'Nelson Agholor', 'Sterling Shepard', 'DeSean Jackson', 'Mohamed Sanu', 'Josh Doctson', 'Rishard Matthews', 'Cameron Meredith', 'Allen Hurns', 'Martavis Bryant', 'D.J. Moore', 'Calvin Ridley', 'Kenny Stills', 'Dede Westbrook', 'Mike Williams', 'Paul Richardson']

ESte = ['Rob Gronkowski', 'Travis Kelce', 'Zach Ertz', 'Greg Olsen', 'Evan Engram', 'Hunter Henry', 'Delanie Walker', 'Jimmy Graham', 'Kyle Rudolph', 'Jack Doyle', 'Trey Burton', 'Jordan Reed', 'Charles Clay', 'Tyler Eifert', 'David Njoku', 'Cameron Brate', 'George Kittle', 'O.J. Howard', 'Austin Seferian-Jenkins', 'Jared Cook', 'Austin Hooper', 'Eric Ebron', 'Ricky Seals-Jones', 'Benjamin Watson', 'Hayden Hurst', 'Vance McDonald', 'Mike Gesicki', 'Rico Gathers', 'Jake Butt', 'Gerald Everett']

ESde = ['Jaguars', 'Eagles', 'Vikings', 'Rams', 'Ravens', 'Chargers', 'Texans', 'Broncos', 'Panthers', 'Saints', 'Steelers', 'Patriots', 'Seahawks', 'Bears', 'Lions', 'Cardinals', 'Titans', 'Falcons', 'Chiefs', 'Bills']

FPde = ['Jaguars', 'Vikings', 'Eagles', 'Rams', 'Texans', 'Broncos', 'Chargers', 'Ravens', 'Seahawks', 'Chiefs', 'Patriots', 'Saints', 'Steelers', 'Panthers', 'Bears', 'Cardinals', 'Falcons', 'Giants', 'Bengals', 'Packers', 'Titans', 'Bills', 'Buccaneers', 'Lions', '49ers', 'Browns', 'Redskins', 'Jets', 'Cowboys', 'Raiders', 'Dolphins', 'Colts']

FCde = ['Jaguars', 'Rams', 'Vikings', 'Texans', 'Eagles', 'Chargers', 'Ravens', 'Broncos', 'Panthers', 'Saints', 'Chiefs', 'Steelers', 'Patriots', 'Seahawks', 'Bears', 'Titans', 'Lions', 'Cardinals', 'Browns', 'Packers', 'Cowboys', 'Giants', 'Bills', 'Bengals', 'Colts', 'Dolphins', 'Jets', 'Raiders', '49ers', 'Buccaneers', 'Redskins', 'Falcons']


holdranks = {}
holdArray = []

def removeExtras(arr):
	for x in range(len(arr)):
		for char in arr[x]:
			if char in ".'":
				arr[x] = arr[x].replace(char,'')
	return arr

def indexItem(start, source, x):
	try:
		return source.index(start[x]) + 1
	except:
		return '-'

def ranks(start, src2, src3):
	for x in range(len(start)):
		total = indexItem(start, start, x)
		count = 1
		std = 0
		stdArr = []
		stdArr.append(total)
		for y in (src2, src3):
			try:
				total += indexItem(start, y, x)
				count += 1
				stdArr.append(indexItem(start, y, x))
			except:
				pass

		avg = round(total/count,2)
		if len(stdArr) > 1:
			for z in range(len(stdArr)):
				std += (stdArr[z] - avg)**2
			std = (std/(len(stdArr) - 1))**.5

		holdranks[start[x]] = {'FP' : indexItem(start, start, x), 'ES' : indexItem(start, src2, x), 'FC' : indexItem(start, src3, x), 'AVG' :avg, 'STD' :round(std,2)}
		holdArray.append({'name' : start[x], 'FP' : indexItem(start, start, x), 'ES' : indexItem(start, src2, x), 'FC' : indexItem(start, src3, x), 'AVG' :avg, 'STD' :round(std,2)})


ranks(removeExtras(FPte), removeExtras(ESte), removeExtras(FCte))
print(holdArray)











# newRanks = sorted(rbRanks, key=lambda x: (rbRanks[x]['AVG']))
# print(newRanks)


# for x in range(len(newRanks)):
# 	print(deRanks[newRanks[x]])


# for x in range(len(ESde)):
# 	deRanks[ESde[x]] = {'ES' : ESde.index(ESde[x]) + 1, 'FP' : FPde.index(ESde[x]) + 1, 'FC' : FCde.index(ESde[x]) + 1}

# print(deRanks)

