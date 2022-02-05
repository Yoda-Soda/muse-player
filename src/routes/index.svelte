<script>
	import { onMount } from 'svelte';
	let topSongName;
	let title;

	onMount(async () => {
		const response = await fetch('http://127.0.0.1:5002/music/Three');
		// const response = await fetch('https://api.publicapis.org/entries');
		const songs = await response.json();
		// topSongName = songs;
		topSongName = songs[0];
		console.log(typeof title, songs);
	});
</script>

<section>
	<h1>Muse Player</h1>
	<h2>TopSong</h2>
	<input type="search" name="" id="" placeholder="Search Song" />
	<code>
		{#if topSongName === undefined}
			Loading Song Name...
		{:else}
			{topSongName.title}
		{/if}
	</code>
</section>

<style>
	section {
		display: grid;
		align-content: center;
		max-width: 500px;
	}
	code {
		background-color: black;
		color: blanchedalmond;
		padding: 3rem;
	}
</style>
