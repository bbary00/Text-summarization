import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {TextService} from '../../services/text.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {
  holdText: FormGroup;

  constructor(private formBuilder: FormBuilder, private textService: TextService) { }

  ngOnInit() {
    this.holdText = this.formBuilder.group({
      text: ['', [Validators.required]],
      sentences: ['', [Validators.required]],
      percent: ['', [Validators.required]]
    });
  }

  onAddText(form) {
    this.textService.setText({
      text: form.text,
      sentences: form.sentences,
      percent: form.sentences
    });

    this.holdText.get('text').setValue('');
    this.holdText.get('sentences').setValue('');
    this.holdText.get('percent').setValue('');
  }

}

