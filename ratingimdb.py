Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import imdb
>>> s=imdb.IMDb()
>>> search=s.get_top250_movies()
>>> for i in range(25):
	print(search[i])

	
The Shawshank Redemption
The Godfather
The Godfather: Part II
The Dark Knight
12 Angry Men
Schindler's List
The Lord of the Rings: The Return of the King
Pulp Fiction
The Good, the Bad and the Ugly
The Lord of the Rings: The Fellowship of the Ring
Fight Club
Forrest Gump
Inception
Star Wars: Episode V - The Empire Strikes Back
The Lord of the Rings: The Two Towers
The Matrix
Goodfellas
One Flew Over the Cuckoo's Nest
Seven Samurai
Se7en
Life Is Beautiful
City of God
The Silence of the Lambs
It's a Wonderful Life
Star Wars: Episode IV - A New Hope
>>> 
