import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { UploadComponent } from './upload/upload.component';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { JsonPipe } from './json.pipe'; // Импорт нового пайпа

@NgModule({
  declarations: [
    AppComponent,
    UploadComponent,
    JsonPipe // Зарегистрируйте пайп здесь
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    CommonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
