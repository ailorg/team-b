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
    <ManyCard :lectures="lectures" label="Lectures" name="Lectures"></ManyCard>

    <div class="section">
      <div class="container text-center">
      </div>
    </div>
  </div>
</template>
<script>
import Vue from 'vue'
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
import data from '../assets/data.json'
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
  },
  data () {
    return{
      lectures: data.lectures,
    }
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
