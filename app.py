from flask import Flask, render_template, url_for

app = Flask(__name__)

# Placeholder routes for all links in the navigation/footer
# These will be implemented properly as each page is converted
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enya-songs-albums.html')
def songs_albums():
    # TODO: Create and render songs_albums.html
    return "Page: Enya Songs & Albums (TODO)"

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
    # TODO: Create and render the-memory-of-trees.html
    return "Page: Album - The Memory of Trees (TODO)"

@app.route('/paint-the-sky-with-stars.html')
def album_paint_the_sky_with_stars():
    # TODO: Create and render paint-the-sky-with-stars.html
    return "Page: Album - Paint The Sky With Stars (TODO)"

@app.route('/a-day-without-rain.html')
def album_a_day_without_rain():
    # TODO: Create and render a-day-without-rain.html
    return "Page: Album - A Day Without Rain (TODO)"

@app.route('/enya-amarantine.html')
def album_amarantine():
    # TODO: Create and render enya-amarantine.html
    return "Page: Album - Amarantine (TODO)"

@app.route('/and-winter-came.html')
def album_and_winter_came():
    # TODO: Create and render and-winter-came.html
    return "Page: Album - And Winter Came (TODO)"

@app.route('/very-best-enya.html')
def album_very_best_enya():
    # TODO: Create and render very-best-enya.html
    return "Page: Album - The Very Best of Enya (TODO)"

@app.route('/enya-dark-sky-island.html')
def album_dark_sky_island():
    # TODO: Create and render enya-dark-sky-island.html
    return "Page: Album - Dark Sky Island (TODO)"

@app.route('/enya-other.html')
def other_songs():
    # TODO: Create and render enya-other.html
    return "Page: Other Songs (TODO)"

@app.route('/all-enya-songs.html')
def all_songs():
    # TODO: Create and render all-enya-songs.html
    return "Page: All Enya Songs (TODO)"

@app.route('/enya-biography.html')
def biography():
    return render_template('biography.html')

@app.route('/new-age-music.html')
def new_age_music():
    # TODO: Create and render new-age-music.html
    return "Page: New Age Music (TODO)"

@app.route('/enya-video.html')
def videos():
    # TODO: Create and render enya-video.html
    return "Page: Videos (TODO)"

@app.route('/sitemap.html')
def sitemap():
    # TODO: Create and render sitemap.html
    return "Page: Sitemap (TODO)"

@app.route('/roma-ryan-nicky.html')
def roma_ryan_nicky():
    # TODO: Create and render roma-ryan-nicky.html
    return "Page: Roma Ryan & Nicky Ryan (TODO)"

@app.route('/enya-quotes.html')
def enya_quotes():
    # TODO: Create and render enya-quotes.html
    return "Page: Enya Quotes (TODO)"

@app.route('/the-lord-of-the-rings.html')
def the_lord_of_the_rings():
    # TODO: Create and render the-lord-of-the-rings.html
    return "Page: The Lord of the Rings (TODO)"

@app.route('/enya-clannad.html')
def enya_clannad():
    # TODO: Create and render enya-clannad.html
    return "Page: Enya & Clannad (TODO)"

@app.route('/the-celts-documentary.html')
def the_celts_documentary():
    # TODO: Create and render the-celts-documentary.html
    return "Page: The Celts Documentary (TODO)"

@app.route('/enya-links.html')
def links():
    return render_template('links.html')

@app.route('/pp.html')
def pp():
    # TODO: Create and render pp.html (Privacy Policy)
    return "Page: Privacy Policy (TODO)"

if __name__ == '__main__':
    app.run(debug=True)
