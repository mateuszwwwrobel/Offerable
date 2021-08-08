import { Component, OnInit } from '@angular/core';
import { RestApiService } from "../shared/rest-api.service";

@Component({
  selector: 'app-offer-list',
  templateUrl: './offer-list.component.html',
  styleUrls: ['./offer-list.component.css']
})
export class OfferListComponent implements OnInit {

  Offer: any = [];
  Categories: any = [];
  searchCategory = 'All';

  constructor(
    public restApi: RestApiService
  ) { }

  ngOnInit() {
    this.loadOffers()
    this.loadCategories()
  }

  loadOffers() {
    return this.restApi.getOffers().subscribe(
      data => {
        this.Offer = data;
      }
    )
  }

  loadCategories() {
    return this.restApi.getCategories().subscribe(
      data => {
        this.Categories = data;
      }
    )
  }

}
