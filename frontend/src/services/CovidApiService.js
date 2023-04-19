/*The code defines a class CovidApiService with several static
methods that make HTTP requests to a COVID-19 statistics API.
The getWorldData() method retrieves global COVID-19 statistics,
getSingleCountryStats(countryName) retrieves statistics for a specific country,
and sendContactEmail(formData) sends a contact form email to the backend API. */

import axios from "axios";

export class CovidApiService {
  static baseUrl = "http://0.0.0.0:8000/v1/countries";

  static getWorldData() {
    return axios.get(`${this.baseUrl}/world`);
  }

  static getSingleCountryStats(countryName) {
    return axios.get(`${this.baseUrl}/${countryName}`);
  }
}
