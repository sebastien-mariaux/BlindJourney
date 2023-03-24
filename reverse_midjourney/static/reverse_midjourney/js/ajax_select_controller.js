import { Controller } from "https://unpkg.com/@hotwired/stimulus/dist/stimulus.js"


export default class ajaxSelectController extends Controller {
  static targets = ["input", 'results']
  static values = { url: String, name: String, id: String, current: String }

  connect() {
    console.log(this.urlValue)
    this.inputTarget.addEventListener('focus', () => {
      this.inputTarget.value = '';
    })
    this.inputTarget.addEventListener('input', (event) => {
      this.fetchData(event.target.value)
    })
    this.inputTarget.addEventListener('blur', () => {
      setTimeout(() => {
        this.inputTarget.value = this.currentValue
        this.resultsTarget.innerHTML = ''
        this.resultsTarget.classList.add('hidden')
      }, 200)
    })
  }

  fetchData(query) {
    const params = new URLSearchParams({
      query: query,
    })
    fetch(this.urlValue + '?' + params)
      .then(response => response.json())
      .then((data) => {
        this.handleResults(data)
      })
  }

  handleResults(data) {
    this.resultsTarget.classList.remove('hidden')
    if (data.results.length > 0) {
      const className = this.getClassName()
      this.resultsTarget.innerHTML = data.results.map((result) => {
        return `<option class=${className} value=${result.pk}>${result.name}</option>`
      }).join('')
      Array.from(document.getElementsByClassName(className)).forEach((element) => {
        element.addEventListener('click', (event) => {
          this.selectGenus(event)
        })
      })
    } else {
      this.resultsTarget.innerHTML = 'No results found'
    }
  }

  selectGenus(event) {
    console.log('selectGenus')
    const pk = event.target.value
    const name = event.target.innerHTML
    this.inputTarget.value = name
    this.currentValue = name
    document.getElementById(this.idValue).value = pk
    this.resultsTarget.innerHTML = ''
    this.resultsTarget.classList.add('hidden')
  }

  getClassName() {
    return this.nameValue + '-option'
  }
}