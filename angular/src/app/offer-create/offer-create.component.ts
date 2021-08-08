import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router';
import { RestApiService } from '../shared/rest-api.service';
import { Category } from '../shared/offer';

@Component({
  selector: 'app-offer-create',
  templateUrl: './offer-create.component.html',
  styleUrls: ['./offer-create.component.css']
})
export class OfferCreateComponent implements OnInit {

  @Input() offerDetails = { title: '', description: '', price: 0, category: '' }
  Categories: any = [];

  constructor(
    public restApi: RestApiService, 
    public router: Router
  ) { }

  ngOnInit() {
    this.loadCategories()
  }

  addOffer(dataOffer?: any) {
    console.log(dataOffer)
    this.restApi.createOffer(this.offerDetails).subscribe((data: {}) => {
      this.router.navigate(['/offers-list'])
    })
  }

  loadCategories() {
    return this.restApi.getCategories().subscribe(
      data => {
        this.Categories = data;
      }
    )
  }

}
