import axios from "axios";

export class CovidApiService {
  static baseUrl = "http://0.0.0.0:8000/v1/emails";

  static sendEmail(emailData) {
    return axios.post(`${this.baseUrl}/send`, emailData);
  }
}
