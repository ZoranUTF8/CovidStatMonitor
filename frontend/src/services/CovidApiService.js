import axios from "axios";

export class CovidApiService {
  static baseUrl = "http://127.0.0.1:8000/v1/countries";

  static getWorldData() {
    return axios.get(`${this.baseUrl}/world`);
  }

  static getSingleCountryStats(countryName) {
    return axios.get(`${this.baseUrl}/${countryName}`);
  }
}
