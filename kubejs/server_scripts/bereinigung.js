// Sky and Stone – Bereinigung (Testserver-Log 25.10.2026)
// ProductiveBees bringt ein Zentrifugen-Rezept für Modularbees mit, Modularbees ist im Pack nicht drin.
// Das Rezept kann nie gebaut werden und erzeugt nur einen Fehler beim Laden.

ServerEvents.recipes(event => {
  event.remove({ id: 'productivebees:centrifuge/modularbees/honeycomb_imperial' })
})
