from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
  date = datetime.datetime.now()
  h = date.hour
  m = date.minute
  s = date.second
  return render_template("index.html", heure = h, minute = m, seconde = s)

@app.route('/resultat',methods = ['GET'])
def resultat():
  result=request.args
  n = result['nom']
  p = result['prenom']
  return render_template("resultat.html", nom=n, prenom=p)
#-----------------------------------------------------------------------------------------------------




#carreau = K
#0 = 10
#all_players = [["Toto", ['3T', '4R']]]

all_cards = ['3T', '3P', '3C', '3K', '4T', '4P', '4C', '4K', '5T', '5P', '5C', '5K', '6T', '6P', '6C', '6K', '7T', '7P', '7C', '7K', '8T', '8P', '8C', '8K', '9T', '9P', '9C', '9K', '0T', '0P', '0C', '0K', 'VT', 'VP', 'VC', 'VK', 'DT', 'DP', 'DC', 'DK', 'RT', 'RP', 'RC', 'RK', 'AT', 'AP', 'AC', 'AK', '2T', '2P', '2C', '2K']
all_players = []
selected_player_id = 0

// AJOUTER LES JOUEURS


// DISTRIBUER LES CARTES
sorted(all_cards)
for card in all_cards:
	all_players[selected_player_id][1].append(card)
	selected_player_id += 1
	if selected_player_id > len(all_players)-1:
		selected_player_id = 0
selected_player_id = 0





#-----------------------------------------------------------------------------------------------------
app.run()
