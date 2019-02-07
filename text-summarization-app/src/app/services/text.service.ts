import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TextService {

  private texts: Text[] = [];

  constructor() { }

  getTexts() {
    return [...this.texts];
  }

  setText(value) {
    this.texts.unshift(value);
  }
}
