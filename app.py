from flask import Flask, render_template, url_for

app = Flask(__name__)

# Placeholder routes for all links in the navigation/footer
# These will be implemented properly as each page is converted
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enya-songs-albums.html')
def songs_albums():
    return render_template('enya-songs-albums.html')

@app.route('/enya-album.html')
def album_enya():
    return render_template('album_enya.html')

@app.route('/watermark.html')
def album_watermark():
    return render_template('album_watermark.html')

@app.route('/shepherd-moons.html')
def album_shepherd_moons():
    return render_template('album_shepherd_moons.html')

@app.route('/the-celts.html')
def album_the_celts():
    return render_template('album_the_celts.html')

@app.route('/the-memory-of-trees.html')
def album_the_memory_of_trees():
    return render_template('the-memory-of-trees.html')

@app.route('/paint-the-sky-with-stars.html')
def album_paint_the_sky_with_stars():
    return render_template('paint-the-sky-with-stars.html')

@app.route('/a-day-without-rain.html')
def album_a_day_without_rain():
    return render_template('a-day-without-rain.html')

@app.route('/enya-amarantine.html')
def album_amarantine():
    return render_template('enya-amarantine.html')

@app.route('/and-winter-came.html')
def album_and_winter_came():
    return render_template('and-winter-came.html')

@app.route('/very-best-enya.html')
def album_very_best_enya():
    return render_template('very-best-enya.html')

@app.route('/enya-dark-sky-island.html')
def album_dark_sky_island():
    return render_template('enya-dark-sky-island.html')

@app.route('/enya-other.html')
def other_songs():
    return render_template('enya-other.html')

@app.route('/all-enya-songs.html')
def all_songs():
    return render_template('all-enya-songs.html')

@app.route('/enya-biography.html')
def biography():
    return render_template('biography.html')

@app.route('/new-age-music.html')
def new_age_music():
    return render_template('new-age-music.html')

@app.route('/enya-video.html')
def videos():
    return render_template('enya-video.html')

@app.route('/sitemap.html')
def sitemap():
    return render_template('sitemap.html')

@app.route('/roma-ryan-nicky.html')
def roma_ryan_nicky():
    return render_template('roma-ryan-nicky.html')

@app.route('/enya-quotes.html')
def enya_quotes():
    return render_template('enya-quotes.html')

@app.route('/the-lord-of-the-rings.html')
def the_lord_of_the_rings():
    return render_template('the-lord-of-the-rings.html')

@app.route('/enya-clannad.html')
def enya_clannad():
    return render_template('enya-clannad.html')

@app.route('/the-celts-documentary.html')
def the_celts_documentary():
    return render_template('the-celts-documentary.html')

@app.route('/enya-links.html')
def links():
    return render_template('links.html')

@app.route('/pp.html')
def pp():
    return render_template('pp.html')

if __name__ == '__main__':
    app.run(debug=True)
