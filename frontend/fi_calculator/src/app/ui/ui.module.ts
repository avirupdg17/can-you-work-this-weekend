import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from '../material/material.module';
import { NavbarComponent } from './navbar/navbar.component';
import { SidenavComponent } from './sidenav/sidenav.component';

@NgModule({
  declarations: [NavbarComponent, SidenavComponent],
  imports: [CommonModule, MaterialModule],
  exports: [NavbarComponent, SidenavComponent],
})
export class UiModule {}
