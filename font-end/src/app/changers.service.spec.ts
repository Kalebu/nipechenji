import { TestBed } from '@angular/core/testing';

import { ChangersService } from './changers.service';

describe('ChangersService', () => {
  let service: ChangersService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ChangersService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
