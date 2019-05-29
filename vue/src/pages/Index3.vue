<template>
  <div>

    <div class="bg">
    <div class="page-header clear-filter" filter-color="orange">
      <MainNavbar/>
      <parallax
        class="page-header-image"
        style="background-image:url('../img/header.jpg')"
      >
      </parallax>
      <div class="container">
        <div class="content-center brand">
          <img  src="../img/psi.png" width="30%" height="30%" alt="" />
          <h1 class="h1-seo"></h1>
          <h3></h3>
          <div class="col-md-12">
            <fg-input
              addon-left-icon="now-ui-icons ui-1_zoom-bold"
              placeholder=""
              class="no-border"/>
          </div>
        </div>
      </div>
    </div>
    <div class="main">
     
    </div>
    <ManyCard/>
    <basic-elements></basic-elements>
    <navigation></navigation>
    <tabs-section></tabs-section>
    <progress-pagination></progress-pagination>
    <notifications></notifications>
    <typography></typography>
    <javascript-components></javascript-components>
    <carousel-section></carousel-section>
    <nucleo-icons-section></nucleo-icons-section>
    <div class="section">
      <div class="container text-center">
        <div class="row justify-content-md-center">
          <div class="col-md-12 col-lg-8">
            <h2 class="title">Completed with examples</h2>
            <h5 class="description">
              The kit comes with three pre-built pages to help you get started
              faster. You can change the text and images and you're good to go.
              More importantly, looking at them will give you a picture of what
              you can built with this powerful Bootstrap 4 ui kit.
            </h5>
          </div>
        </div>
      </div>
    </div>
    <signup-form></signup-form>
    <examples-section></examples-section>
    <download-section></download-section>
  </div>
</template>
<script>
import  { Parallax } from '@/components';
import BasicElements from './components/BasicElementsSection';
import Navigation from './components/Navigation';
import TabsSection from './components/Tabs';
import ProgressPagination from './components/ProgressPagination';
import Notifications from './components/Notifications';
import Typography from './components/Typography';
import JavascriptComponents from './components/JavascriptComponents';
import CarouselSection from './components/CarouselSection';
import NucleoIconsSection from './components/NucleoIconsSection';
import SignupForm from './components/SignupForm';
import ExamplesSection from './components/ExamplesSection';
import DownloadSection from './components/DownloadSection';
import MainNavbar from '@/layout/MainNavbar.vue';
import ManyCard from '@/components/Cards/ManyCard';
import {
  Button,
  Checkbox,
  Radio,
  FormGroupInput,
  Slider,
  Switch
} from '@/components';

export default {
  name: 'index',
  bodyClass: 'index-page',
  components: {
    [FormGroupInput.name]: FormGroupInput,
    ManyCard,
    MainNavbar,
    Parallax,
    BasicElements,
    Navigation,
    TabsSection,
    ProgressPagination,
    Notifications,
    Typography,
    JavascriptComponents,
    CarouselSection,
    NucleoIconsSection,
    SignupForm,
    ExamplesSection,
    DownloadSection
  }
};
</script>
<style>

.bg{
  background-image:url('../img/haikei2.jpg');
  background-size: contain
}

.page-header{
  background-image:url('../img/haikei2.jpg');
  background-size: contain
}

</style>
